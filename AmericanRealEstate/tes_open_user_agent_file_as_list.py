invalidation_user_agent_list = []
with open('./invalidation_user_agent_file.txt','r') as f:
    for user_agent in f.readlines():

        print(user_agent)
        invalidation_user_agent_list.append(user_agent)