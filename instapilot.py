#import

import os, sys, subprocess, importlib.util, time

#req

class fg:
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    RESET   = '\033[39m'

def typewriter(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.01)
    print()

package_names = ["instagrapi", "requests"]

InsPi = '''
\033[32m
 .___                 __        __________.__.__          __ 
 |   | ____   _______/  |______ \______   \__|  |   _____/  |_ 
 |   |/    \ /  ___/\   __\__  \ |     ___/  |  |  /  _ \   __\ 
 |   |   |  \/___ \  |  |  / __ \|    |   |  |  |_(  <_> )  | 
 |___|___|  /____  > |__| (____  /____|   |__|____/\____/|__| 
          \/     \/            \/ 
 <------------------------------------------------------------>
 | GitHub : TnYtCoder               |       MIT License       |
 | Instagram Automated Python Tool  |        Instagrapi       |
 +------------------------------------------------------------+
'''

#installations & logo

time.sleep(1)
os.system("clear")
time.sleep(1)

typewriter(InsPi)

time.sleep(1)
print("\n\033[35m[+] Checking Requirements \n")
time.sleep(2)

for package_name in package_names:
        if importlib.util.find_spec(package_name):
                print(f"\n\033[32m[+] {package_name} Is Installed ;)\n")
        else:
                print(f"\n\033[31m[×] {package_name} Is Not Installed :/")
                try:
                        print(f"\033[35m[+] Installing {package_name}")
                        subprocess.run(["pip3", "install", package_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
                        print(f"\033[32m[+] {package_name} Installed Successfully !\n")
                        import instagrapi
                        from instagrapi import Client
                except subprocess.CalledProcessError:
                        print("\033[31m Please Install Packages Manually")
                        sys.exit(1)

import instagrapi
from instagrapi import Client
cl = Client()

time.sleep(1)
os.system('clear')
print(InsPi)
time.sleep(1)

#process

print("\n\033[33m [+] Login")
usr = input("\n\033[35m username : \033[31m")
pas = input("\033[35m password : \033[31m")

try:
	cl.login(usr, pas)
	print("\n\033[32m [+] Login Successful !")
except instagrapi.exceptions.BadPassword:
	print("\n\033[31m [+] Please Check Your Password !")
	sys.exit()
except instagrapi.exceptions.RateLimitError:
	print("\n\033[31m [+] Too Many Login Attempts, Please Try Later !")
	sys.exit()
except instagrapi.exceptions.PleaseWaitFewMinutes:
	print("\n\033[31m [+] Please Try After Few Minutes !")
	sys.exit()
except instagrapi.exceptions.ClientConnectionError:
	print("\n\033[31m [+] Please Check You Internet Connection !")
	sys.exit()
except instagrapi.exceptions.ChallengeUnknownStep:
	print("\n\033[31m [+] Instagram Needs Phone Number Verification !")
	sys.exit()
except instagrapi.exceptions.ProxyAddressIsBlocked:
	print("\n\033[31m [+] Instagram Has Blocked Your IP Address, Use Proxy To Bypass !")
except KeyboardInterrupt:
	print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
	sys.exit()

def conexit():
	con = input("\n\033[34m Do You Want To Continue (Y/n) : ")

	if con == "Y" or con == "y":
		time.sleep(1)
		os.system("clear")
		Main()
	else:
		cne = "\n\033[32m [+] Thank You For Using !!"
		typewriter(cne)

def follow(username):
	try:
		x = username
		try:
			y = cl.user_id_from_username(x)
			cl.user_follow(y)
			print("\n\033[36m User Followed !")
		except Exception as e:
			print("\n\033[31m Error" + e)
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()

def follow_user_list(filename):
	try:
		x = filename
		with open(x, "r") as f:
			user_list = f.read().splitlines()

		user_id = [cl.user_id_from_username(user) for user in user_list]
		for usertof in user_id:
			try:
				print(f"\n\033[36m Trying To Follow User : {usertof}")
				cl.user_follow(usertof)
				print(" User Followed !")
			except instagrapi.exceptions.UserNotFound:
				print("\n\033[31m User Not Found !")
			except instagrapi.exceptions.ClientNotFoundError:
				print("\n\033[31m Client Not Found !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()

def unfollow_user(target):
	try:
		unfollow_user_id = cl.user_id_from_username(target)
		try:
			print(f"\n\033[36m Trying To Unfollow User : {unfollow_user_id}")
			cl.user_unfollow(unfollow_user_id)
			print(" User Unfollowed !")
		except instagrapi.exceptions.UserNotFound:
			print("\n\033[31m User Not Found !")
		except instagrapi.exceptions.ClientNotFoundError:
			print("\n\033[31m Client Not Found !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()

def remove_follower(target):
	try:
		user_id = cl.user_id_from_username(target)
		try:
			print(f"\n\033[36m Trying To Remove Follower : {user_id}")
			cl.user_remove_follower(user_id)
			print(" Follower Removed !")
		except instagrapi.exceptions.UserNotFound:
			print("\033[31m User Not Found !")
		except instagrapi.exceptions.ClientNotFoundError:
			print("\n\033[31m Client Not Found !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()

def remove_all_followers():
	try:
		user_id = cl.user_id_from_username(usr)
		print("\n\033[36m Fetching Info... ('This May Take Time') ! \n")
		followers = cl.user_followers(user_id)
		followers_ids = list(followers.keys())

		for f_to_removed in followers_ids:
			try:
				print(f"\n\033[36m Trying To Remove Followers : {f_to_removed}")
				cl.user_remove_follower(f_to_removed)
				print(" Follower Removed !")
			except instagrapi.exceptions.UserNotFound:
				print("\033[31m User Not Found !")
			except instagrapi.exceptions.ClientNotFoundError:
				print("\n\033[31m Client Not Found !")
			except instagrapi.exceptions.PleaseWaitFewMinutes:
				print("\n\033[31m Please Try Again After Few Minutes !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()

def unfollow_all_user():
	try:
		user_id = cl.user_id_from_username(usr)
		print("\n\033[36m Fetching Info... ('This May Take Time') ! \n")
		followings = cl.user_following(user_id)
		followings_ids = list(followings.keys())

		for u_to_unfollow in followings_ids:
			try:
				print(f"\n\033[36m Trying To Unfollow User : {u_to_unfollow}")
				cl.user_unfollow(u_to_unfollow)
				print(" User Unfollowed !")
			except instagrapi.exceptions.UserNotFound:
				print("\033[31m User Not Found !")
			except instagrapi.exceptions.ClientNotFoundError:
				print("\n\033[31m Client Not Found !")
			except instagrapi.exceptions.PleaseWaitFewMinutes:
				print("\n\033[31m Please Try Again After Few Minutes !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()

def follow_user_following(target):
	try:
		user_id = cl.user_id_from_username(target)
		followings = cl.user_following(user_id)
		followings_ids = list(followings.keys())

		for u_to_follow in followings_ids:
			try:
				print(f"\n\033[36m Trying To Follow User : {u_to_follow}")
				cl.user_follow(u_to_follow)
				print(" User Followed !")
			except instagrapi.exceptions.UserNotFound:
				print("\033[31m User Not Found !")
			except instagrapi.exceptions.PleaseWaitFewMinutes:
				print("\n\033[31m Please Try Again After Few Minutes !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()
	except instagrapi.exceptions.UserNotFound:
		print("\n\033[31m User Not Found !")

def follow_user_followers(target):
	try:
		user_id = cl.user_id_from_username(target)
		followers = cl.user_followers(user_id)
		followers_ids = list(followers.keys())

		for u_to_follow in followers_ids:
			try:
				print(f"\n\033[36m Trying To Follow User : {u_to_follow}")
				cl.user_follow(u_to_follow)
				print("User Followed !")
			except instagrapi.exceptions.UserNotFound:
				print("\033[31m User Not Found !")
			except instagrapi.exceptions.PleaseWaitFewMinutes:
				print("\n\033[31m Please Try Again After Few Minutes !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()
	except instagrapi.exceptions.UserNotFound:
		print("\n\033[31m User Not Found !")

def get_user_id_from_username(target):
	try:
		user_id = cl.user_id_from_username(target)
		print(f"\n\033[36m User_Id : {user_id}")
	except instagrapi.exceptions.UserNotFound:
		print("\033[31m User Not Found !")
	except instagrapi.exceptions.PleaseWaitFewMinutes:
		print("\n\033[31m Please Try Again After Few Minutes !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()
	except instagrapi.exceptions.UserNotFound:
		print("\n\033[31m User Not Found !")

def get_username_from_user_id(target):
	try:
		username = cl.username_from_user_id(target)
		print(f"\n\033[36m Username : {username}")
	except instagrapi.exceptions.UserNotFound:
		print("\033[31m User Not Found !")
	except instagrapi.exceptions.PleaseWaitFewMinutes:
		print("\n\033[31m Please Try Again After Few Minutes !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()
	except instagrapi.exceptions.UserNotFound:
		print("\n\033[31m User Not Found !")

def user_following_into_list(target):
	try:
		print("\n\033[36m Fetching Info... ('This May Take Time') !")
		user_id = cl.user_id_from_username(target)
		followings = cl.user_following(user_id)
		followings_ids = list(followings.keys())
		followings_username = []

		for usernames in followings_ids:
			try:
				username = cl.username_from_user_id(usernames)
				followings_username.append(username)
			except instagrapi.exceptions.UserNotFound:
				print("\033[31m User Not Found !")

		filename = f"{user_id}_following.txt"

		with open(filename, "w") as file:
			for user_names in followings_username:
				file.write(username + "\n")

		print(f"\n\033[36m File Saved As : {filename}")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def user_followers_into_list(target):
	try:
		print("\n\033[36m Fetching Info... ('This May Take Time') !")
		user_id = cl.user_id_from_username(target)
		followers = cl.user_followers(user_id)
		followers_ids = list(followers.keys())
		followers_username = []

		for usernames in followers_ids:
			try:
				username = cl.username_from_user_id(usernames)
				followers_username.append(username)
			except instagrapi.exceptions.UserNotFound:
				print("\033[31m User Not Found !")

		filename = f"{user_id}_followers.txt"

		with open(filename, "w") as file:
			for user_names in followers_username:
				file.write(user_names + "\n")

		print(f"\n\033[36m File Saved As : {filename}")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def like_media(url):
	try:
		media_id = cl.media_pk_from_url(url)
		cl.media_like(media_id)
		print(f"\n\033[36m Media Liked !")
	except instagrapi.exceptions.MediaError:
		print("\n\033[31m Media Error Received From Instagram")
	except instagrapi.exceptions.MediaNotFound:
		print("\n\033[31m Media Not Found !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()

def like_all_media(target):
	try:
		user_id = cl.user_id_from_username(target)
		media_list = cl.user_medias(user_id)
		media_pk = []

		for media in media_list:
			media_pk.append(media.pk)

		for media_x in media_pk:
			try:
				print(f"\n\033[36m Media : {media_x}")
				cl.media_like(media_x)
				print(" Status : Liked !")
			except instagrapi.exceptions.MediaError:
				print("\033[31m Status : Not Liked !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def unlike_media(url):
	try:
		media_id = cl.media_pk_from_url(url)
		cl.media_unlike(media_id)
		print(f"\n\033[36m Media Unliked !")
	except instagrapi.exceptions.MediaError:
		print("\n\033[31m Media Error Received From Instagram")
	except instagrapi.exceptions.MediaNotFound:
		print("\n\033[31m Media Not Found !")
	except KeyboardInterrupt:
		print("\n\033[31m [+] Keyboard Interrupt : Script Ended !")
		sys.exit()

def unlike_all_media(target):
	try:
		user_id = cl.user_id_from_username(target)
		media_list = cl.user_medias(user_id)
		media_pk = []

		for media in media_list:
			media_pk.append(media.pk)

		for media_x in media_pk:
			try:
				print(f"\n\033[36m Media : {media_x}")
				cl.media_unlike(media_x)
				print(" Status : Unliked !")
			except instagrapi.exceptions.MediaError:
				print("\033[31m Status : Not Unliked !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def download_post(url):
	try:
		media_id = cl.media_pk_from_url(url)
		path = "saved_media/"
		try:
			print(f"\n\033[36m Downloading Media : {media_id}")
			post = cl.photo_download(media_id, path)
			print(" Status : Media Downloaded !")
		except instagrapi.exceptions.MediaError:
			print("\033[31m Status : Media Not Downloaded !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def download_reel(url):
	try:
		media_id = cl.media_pk_from_url(url)
		path = "saved_media/"
		try:
			print(f"\n\033[36m Downloading Media : {media_id}")
			post = cl.clip_download(media_id, path)
			print(" Status : Media Downloaded !")
		except instagrapi.exceptions.MediaError:
			print("\033[31m Status : Media Not Downloaded !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def download_video(url):
	try:
		media_id = cl.media_pk_from_url(url)
		path = "saved_media/"
		try:
			print(f"\n\033[36m Downloading Media : {media_id}")
			post = cl.video_download(media_id, path)
			print(" Status : Media Downloaded !")
		except instagrapi.exceptions.MediaError:
			print("\033[31m Status : Media Not Downloaded !")
	except Exception as e:
			print(f"\n\033[31m Error : {str(e)}")

def upload_post(Path, Caption):
	try:
		try:
			print(f"\n\033[36m Uploading Media...")
			cl.photo_upload(path=Path, caption=Caption)
			print(f" Status : Uploaded !")
		except instagrapi.exceptions.MediaError:
			print(f"\n\033[31m Status : Media Not Uploaded !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def upload_reel(Path, Caption):
	try:
		try:
			print(f"\n\033[36m Uploading Media...")
			cl.clip_upload(path=Path, caption=Caption)
			print(f" Status : Uploaded !")
		except instagrapi.exceptions.MediaError:
			print("\n\033[31m Status : Media Not Uploaded !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def upload_video(Path, Caption):
        try:
                try:
                        print(f"\n\033[36m Uploading Media...")
                        cl.video_upload(path=Path, caption=Caption)
                        print(f" Status : Uploaded !")
                except instagrapi.exceptions.MediaError:
                        print("\n\033[31m Status : Media Not Uploaded !")
        except Exception as e:
                print(f"\n\033[31m Error : {str(e)}")

def delete_media(url):
	try:
		media_id = cl.media_pk_from_url(url)
		try:
			print(f"\n\033[36m Deleting Media : {media_id}")
			cl.media_delete(media_id)
			print(" Status : Deleted !")
		except instagrapi.exceptions.MediaError:
			print("\n\033[31m Status : Media Not Uploaded !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def mass_delete_media():
	try:
		user_id = cl.user_id_from_username()
		media_list = cl.user_medias(user_id)
		media_pk = []

		for media in media_pk:
			media_pk.append(media.pk)

		for media_d in media_pk:
			try:
				print(f"\n\033[36m Deleting Media : {media_d}")
				cl.media_delete(media_d)
				print(" Status : Deleted !")
			except instagrapi.exceptions.MediaError:
				print("\n\033[31m Status : Media Not Uploaded !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def media_info(url):
	try:
		media_id = cl.media_pk_from_url(url)
		media_info = cl.media_info(media_id)
		info = f"""\033[36m
 Username : {media_info.user.username}
 Name : {media_info.user.full_name}
 Comments : {media_info.comment_count}
 Likes : {media_info.like_count}
 Caption : {media_info.caption_text}
 Views : {media_info.view_count}
 Duration : {media_info.video_duration}"""
		print(info)
	except Exception as e:
		print(f"\n\033[31m Error : {str(e)}")

def comment(url, comment):
	try:
		media_id = cl.media_pk_from_url(url)
		print(f"\n\033[36m Comment : {comment}")
		cl.media_comment(media_id, comment)
		print(" Status : Done !")
	except Exception as e:
		print(f"\n\033[31m Error : {str(str)}")

def help():
	url = "https://bit.ly/TnYtCoder"
	command = ["am", "start", "-a", "android.intent.action.VIEW", "-d", url]
	subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

time.sleep(1)
os.system("clear")

def Main():
	print(InsPi)
	time.sleep(0.1)
	options = '''\033[33m
 ·————————————————————————————————————·————————————————————————————————————·
 │ [1] Follow User                    │ [21] Upload Reel                   │
 │ [2] Follow User From List          │ [22] Upload Video                  │
 │ [3] Unfollow User                  │ [23] Delete Media                  │
 │ [4] Remove Follower                │ [24] Mass Media Delete             │
 │ [5] Remove All Followers           │ [25] Media Information             │
 │ [6] Unfollow All User              │ [26] Comment                       │
 │ [7] Follow User Following          │                                    │
 │ [8] Follow User Followers          │                                    │
 │ [9] Get User Id From Username      │                                    │
 │ [10] Get Username From User Id     │                                    │
 │ [11] User Following Into List      │                                    │
 │ [12] User Followers Into List      │                                    │
 │ [13] Like Media                    │                                    │
 │ [14] Like All Media                │                                    │
 │ [15] Unlike Media                  │                                    │
 │ [16] Unlike All Media              │                                    │
 │ [17] Download Post                 │                                    │
 │ [18] Download Reel                 │                                    │
 │ [19] Download Video                │                                    │
 │ [20] Upload Post                   │                                    │
 ·————————————————————————————————————·—————————————————————————————————————
 │            \033[31m[00] Exit               \033[33m│              [99] Help             │
 ·——————————————————————————————————————————————————————————————————————————
	'''
	print(options)
	opt = int(input("\033[35m Your Option : "))
	if opt == 1:
		followuser = input("\n\033[33m username : ")
		flu = follow(followuser)
		conexit()

	elif opt == 2:
		followuserlist = input("\n\033[33m file name : ")
		ful = follow_user_list(followuserlist)
		conexit()

	elif opt == 3:
		unfollowuser = input("\n\033[33m username : ")
		uu = unfollow_user(unfollowuser)
		conexit()

	elif opt == 4:
		rmfollowersuser = input("\n\033[33m username : ")
		rfu = remove_follower(rmfollowersuser)
		conexit()

	elif opt == 5:
		remove_all_followers()
		conexit()

	elif opt == 6:
		unfollow_all_user()
		conexit()

	elif opt == 7:
		target = input("\n\033[33m username : ")
		fuf = follow_user_following(target)
		conexit()

	elif opt == 8:
		target = input("\n\033[33m username : ")
		fufs = follow_user_followers(target)
		conexit()

	elif opt == 9:
		target = input("\n\033[33m username : ")
		guifu = get_user_id_from_username(target)
		conexit()

	elif opt == 10:
		target = input("\n\033[33m user id : ")
		gufui = get_username_from_user_id(target)
		conexit()

	elif opt == 11:
		target = input("\n\033[33m username : ")
		ufil = user_following_into_list(target)
		conexit()

	elif opt == 12:
		target = input("\n\033[33m username : ")
		ufil = user_followers_into_list(target)
		conexit()

	elif opt == 13:
		target = input("\n\033[33m url : ")
		lm = like_media(target)
		conexit()

	elif opt == 14:
		target = input("\n\033[33m username : ")
		lam = like_all_media(target)
		conexit()

	elif opt == 15:
		target = input("\n\033[33m url: ")
		um = unlike_media(target)
		conexit()

	elif opt == 16:
		target = input("\n\033[33m username : ")
		ual = unlike_all_media(target)
		conexit()

	elif opt == 17:
		target = input("\n\033[33m url : ")
		dp = download_post(target)
		conexit()

	elif opt == 18:
		target = input("\n\033[33m url : ")
		dr = download_reel(target)
		conexit()

	elif opt == 19:
		target = input("\n\033[33m url : ")
		dv = download_video(target)
		conexit()

	elif opt == 20:
		path = input("\n\033[33m path : ")
		caption = input(" caption : ")
		up = upload_post(path, caption)
		conexit()

	elif opt == 21:
		path = input("\n\033[33m path : ")
		caption = input(" caption : ")
		ur = upload_reel(path, caption)
		conexit()

	elif opt == 22:
		path = input("\n\033[33m path : ")
		caption = input(" caption : ")
		uv = upload_video(path, caption)
		conexit()

	elif opt == 23:
		url = input("\n\033[33m url : ")
		dm = delete_media(url)
		conexit()

	elif opt == 24:
		mass_delete_media()
		conexit()

	elif opt == 25:
		url = input("\n\033[33m url : ")
		mi = media_info(url)
		conexit()

	elif opt == 26:
		url = input("\n\033[33m url : ")
		comment = input(" comment : ")
		c = comment(url, comment)
		conexit()

	elif opt == 00:
		time.sleep(0.5)
		exit = "\n\033[32m [+] Thank You For Using !!"
		typewriter(exit)

	elif opt == 99:
		help()
		conexit()

	else:
		print("\n\033[31m Wrong Options")
		time.sleep(3)
		os.system("clear")
		Main()
Main()

cl.logout()
#ending
