import requests
import pandas as pd
import os
import ast
import time
import cv2
import pafy

TMDB_API_KEY = 'e0476a281215758d95503294fc0cb530' # can be found in the Code -> TMDB folder
TMDB_VIDEO_URL = 'https://api.themoviedb.org/3/movie/{}/videos?api_key={}'

def read_dataset_csv(fileName,header):
  file = pd.read_csv(
    "./Datasets/"+fileName,
    usecols = header,
    index_col=False)
  return file

"""
Use TMDB ID to retrieve Youtube ID from TMDB dataset
"""
def get_youtube_data(video_data,genres):
  trailers = {}
  url_base = 'https://www.youtube.com/watch?v='
  for i, (key, value) in enumerate(video_data.items()):
    try:
      url = TMDB_VIDEO_URL.format(value['id'], TMDB_API_KEY)
      resp = requests.get(url)
      if resp.status_code != 200:
        print('Error: Failed to retrieve video for TMDb ID {} with status code: {}' \
              .format(value['id'], resp.status_code))
        trailers.append([])
      else:
        youtube_results = []  # a list of ids
        for video in resp.json()['results']:
          if video['site'] == 'YouTube' and (video['type'] in {'Teaser', 'Trailer'}) and video['key'] != '':
            youtube_results.append([video['name'], url_base + video['key']])
            break; #add break here because we only want on video for one movie now
        if len(youtube_results) > 0:
          temp = {}
          temp['Youtube Info'] = youtube_results
          temp['Video Info'] = value
          trailers[value['id']] = temp

      # Rate limiting, stall 10 seconds
      if i != 0 and i % 40 == 0:
        print('===================== TMDB Sleep =====================')
        time.sleep(10)
    except:
      print('Send Request Failed')

  return trailers

# def get_youtube_data_harcode(video_data,hard_id):
#   print('get_youtube_data_harcode')
#
#
#   trailers = {}
#   url_base = 'https://www.youtube.com/watch?v='
#   for i, (key, value) in enumerate(video_data.items()):
#     print(value['id'])
#     if value['id'] != hard_id:
#       continue
#
#     try:
#       url = TMDB_VIDEO_URL.format(value['id'], TMDB_API_KEY)
#       resp = requests.get(url)
#       if resp.status_code != 200:
#         print('Error: Failed to retrieve video for TMDb ID {} with status code: {}' \
#               .format(value['id'], resp.status_code))
#         trailers.append([])
#       else:
#         youtube_results = []  # a list of ids
#         for video in resp.json()['results']:
#           if video['site'] == 'YouTube' and (video['type'] in {'Teaser', 'Trailer'}) and video['key'] != '':
#             youtube_results.append([video['name'], url_base + video['key']])
#             print("Find the harcoded movie: ",url_base + video['key'])
#             break
#         if len(youtube_results) > 0:
#           temp = {}
#           temp['Youtube Info'] = youtube_results
#           temp['Video Info'] = value
#           trailers[value['id']] = temp
#
#         break
#     except:
#       print('Send Request Failed')
#
#   return trailers
#

"""
Filters
"""
def genres_filter(data,genres):
  genres_list = ast.literal_eval(data['Video Info']['genres'])
  found = False
  unexpected_list = ['Animation','Fantasy','Science Fiction']
  for each in genres_list:
    if each['name']  in unexpected_list:
      print('Found Unexpected Genre')
      break;
    elif each['name'] in genres :
      found = True
      print('Genres Match')
      break;
  return found

def length_filter(video_streams,length):
  fps = round(video_streams.get(cv2.CAP_PROP_FPS))
  frame_count = int(video_streams.get(cv2.CAP_PROP_FRAME_COUNT))
  video_length = frame_count/fps
  print('Duration: {} sec '.format(video_length) )
  return True if video_length<length else False

"""
Use Pafy & Youtube ID to get youtube video 
"""
def get_video_data(num_videos, length, genres, video_list):
  print('get_video_data , ',num_videos)

  return_video_list = {}
  n = 0
  for i, (key, value) in enumerate(video_list.items()):
    print('------------------ ID {} ------------------'.format(key))
    print('value=',value)
    streams = [];

    # Filter: Genres
    if genres != 'NA':
      temp = genres_filter(value, genres)
      if (temp == False):  # Genres do not match
        continue

    eachVideo = value['Youtube Info'][0]
    url = eachVideo[1]
    try:
      n += 1
      youtube_video = pafy.new(url)
      youtube_video = youtube_video.getbest()
      video_streams = cv2.VideoCapture(youtube_video.url)

     # Filter: Video Length
      if (length_filter(video_streams, length)):
        print('Within Limit')
        streams.append([eachVideo[0], eachVideo[1], youtube_video])
        streams.append([eachVideo[0], eachVideo[1], youtube_video])
    except:
      print('Pafy Get Wrong')

    #To avoid being recognized as robot by youtubedl
    if n != 0 and n % 5 == 0:
      print('===================== Pafy Get Sleep =====================')
      time.sleep(10)

    if len(streams) != 0:
      return_video_list[key] = video_list[key]
      return_video_list[key]['Youtube Info'] = streams.copy()

    if len(return_video_list) >= num_videos:
      print('Found -- {} movies'.format(num_videos))
      break;

  return return_video_list


"""
Download Youtube Video to local
"""
def save_videos(movie_raw_data):

  for i, (key, value) in enumerate(movie_raw_data.items()):
    for j, eachVideo in enumerate(value['Youtube Info']):
      video_data = cv2.VideoCapture(eachVideo[2].url)
      video_name = '\movie_{}_video_{}'.format(i, j)
      fps = video_data.get(cv2.CAP_PROP_FPS)
      width = int(video_data.get(cv2.CAP_PROP_FRAME_WIDTH))
      height = int(video_data.get(cv2.CAP_PROP_FRAME_HEIGHT))
      fourcc = cv2.VideoWriter_fourcc(*'mp4v')
      fileName = os.path.join('C:\CCQ\2020F\capstone\Code\Videos', video_name)
      out = cv2.VideoWriter(fileName, fourcc, fps, (width, height))

      count = 0
      while (1):
        ret, frame = video_data.read()
        if ret == True:
          out.write(frame)
          count+=1
        else:
          break

      print('Processed {} frames'.format(count))

      out.release()

  return

