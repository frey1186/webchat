from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
import time
import queue

# Create your views here.

def chat_index(request):

    return render(request, "chat/chat_index.html")


GLOBAL_QUEUE_LIST = {}
def message_handle(request):

    if request.method == "POST":
        print(request.POST)
        if request.POST.get("msgs"):
            msgs_dict = json.loads(request.POST.get("msgs"))
            msgs_dict["time"] = time.time()
            queue_key = int(msgs_dict["to"])
            if queue_key not in GLOBAL_QUEUE_LIST:
                GLOBAL_QUEUE_LIST[queue_key] = queue.Queue()
            GLOBAL_QUEUE_LIST[queue_key].put(msgs_dict)
            print("msgs-->", msgs_dict)
            print("GLOBAL_QUEUE_LIST-->",GLOBAL_QUEUE_LIST)
        return HttpResponse("post ok")

    elif request.method == "GET":
        user_id = request.user.userprofile.id
        msgs_list=[]
        if user_id not in GLOBAL_QUEUE_LIST:
            GLOBAL_QUEUE_LIST[user_id] = queue.Queue()

        msg_q = GLOBAL_QUEUE_LIST[user_id]
        print("begin->",msg_q,'--------->',request.user)
        try:
            if msg_q.qsize() > 0:
                for i in range(msg_q.qsize()):
                    msgs_list.append(msg_q.get())
            else:
                msgs_list.append(msg_q.get(timeout=60))
        except queue.Empty:
            msgs_list=[]
        print("end->",msg_q,'--------->',request.user)
        return HttpResponse(json.dumps(msgs_list))

