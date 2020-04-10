from django.apps import AppConfig

import os
import re
import pandas as pd
import numpy as np
from InstagramAPI import InstagramAPI



def get_profile_post_list(info_user,api):
  post_list = []
  if info_user["status"] == "ok":
    username_id = info_user['user']['pk'] # Get user ID
    user_posts = api.getUserFeed(username_id)
    user_posts_info = api.LastJson
    #print(user_posts_info.keys())
    if isinstance(user_posts_info,dict) and "items" in user_posts_info:
      post_list = user_posts_info["items"]

  return post_list

def get_hashtag_list_from_post_comments(post,api):
    hashtag_list = []
    #get hashtags from comments
    media_id = post["id"]
    api.getMediaComments(media_id)
    comment_info = api.LastJson
    #print(comment_info.keys())
    if "comments" in comment_info:
      comment_list = comment_info["comments"]
      for comment in comment_list:
        if "text" in comment:
          text = comment["text"]
          hashtag_list += re.findall(r"#(\w+)",text)

    return hashtag_list

def get_hashtag_list_from_post_caption(post):
    hashtag_list = []
    #get hashtags from captions
    key = "caption"
    if key in post.keys():
        caption = post[key]
        if caption and "text" in caption:
          text = caption["text"]
          hashtag_list += re.findall(r"#(\w+)",text)
    return hashtag_list


def get_bio_from_profile(info_user,api):
  bio = ""
  if "status" in info_user and info_user["status"] == "ok":
    username_id = info_user['user']['pk'] # Get user ID
    api.getUsernameInfo(username_id)
    result = api.LastJson
    bio = result["user"]["biography"]
  return bio

def get_unique_hashtag_dict(all_hashtag_list):
  unique_dict = {}
  for el in all_hashtag_list:
    if el in unique_dict.keys():
      unique_dict[el]+= 1
    else:
      unique_dict.update({el:1})

  unique_dict = {k: v for k, v in sorted(unique_dict.items(), key=lambda item: item[1],reverse=True)}
  return unique_dict

def get_info_profile(profile,api):
  api.searchUsername(profile)
  info_user = api.LastJson
  if isinstance(info_user,dict) and "status" in info_user and info_user["status"] == "ok":
    return info_user
  else:
    return {}

def get_hashtags_from_bio(bio):
  return re.findall(r"#(\w+)",bio)


def get_common_hashtag_df(unique_hashtag_list, hashtag_dict_list, total_hashtag_dict, threshold = 1,save = True):
  final_list = []
  for hashtag in unique_hashtag_list:
    user_list = []
    for _hashtag_dict in hashtag_dict_list:
      if hashtag in _hashtag_dict.keys():
        user_list += [_hashtag_dict["user"]]

    if len(user_list) > threshold:
      data_dict = {"hashtag":hashtag,"count":total_hashtag_dict[hashtag],"user_list":user_list}
      final_list.append(data_dict)

  df = pd.DataFrame(final_list)
  if "user_list" in df.columns:
    df["num_users"] = df["user_list"].apply(lambda x:len(x))
    df = df.sort_values(by=['count'],ascending=False)
    df = df.sort_values(by=['num_users'],ascending=False)
    df.index = np.arange(df.shape[0])

    if save:
        os.chdir("/content/drive/My Drive/insta")
        df.to_excel("hashtag.xlsx")

  return df


def get_hashtags(input_text):
    
    api.login()

    profile_list = input_text.split()

    total_hashtag_list = []
    hashtag_dict_list = []
    for i,profile in enumerate(profile_list):

        #print(profile)

        #get profile data
        info_profile = get_info_profile(profile,api)

        if info_profile:

            bio = get_bio_from_profile(info_profile,api)      
            all_hashtag_list = get_hashtags_from_bio(bio)

            post_list = get_profile_post_list(info_profile,api)
            #print("len post list {}".format(len(post_list)))

            for post in post_list:
                all_hashtag_list += get_hashtag_list_from_post_comments(post,api)
                all_hashtag_list += get_hashtag_list_from_post_caption(post)

            hashtag_dict = get_unique_hashtag_dict(all_hashtag_list)
            hashtag_dict.update({"user":profile})
            hashtag_dict_list.append(hashtag_dict)

            #print(hashtag_dict)

            total_hashtag_list += all_hashtag_list

    unique_hashtag_list = list(set(total_hashtag_list))
    #print("number of unique hashtags {}".format(len(unique_hashtag_list)))


    total_hashtag_dict = get_unique_hashtag_dict(total_hashtag_list)


    df = get_common_hashtag_df(unique_hashtag_list, hashtag_dict_list, total_hashtag_dict, threshold = 1,save = False)

    return df


class HashtagAppConfig(AppConfig):
    name = 'hashtag_app'

    message = 'Helloooo'
