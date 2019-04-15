## This is script Omer.ismail 


import boto3
import random
import time
import sys



session=boto3.Session(aws_access_key_id="AKIAJO53UHGYI6A7N4CQ",aws_secret_access_key="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",region_name="eu-west-1")

ec2_re_ob=session.resource(service_name='ec2')
ec2_cli=session.client(service_name="ec2")


expireTIME=600  # CHNAGE IT if HA takes longer time to recover

def get_ec2_running_count(RunningInstances):
    inst_count=0
    #for each_in in ec2_re_ob.instances.all():
    for each_in in RunningInstances:
        #inst_count.append(each_in.id)
        inst_count = inst_count+1
    return(inst_count)


def get_ec2_instances():
    # create filter for instances in running state
    filters = [
        {
            'Name': 'instance-state-name',
            'Values': ['running']
        }
    ]

    # filter the instances based on filters() above
    instances = ec2_re_ob.instances.filter(Filters=filters)
    return instances

def list_running_ec2(RunningInstances):
    # instantiate empty array
    ListRunningInstances = []

    for instance in RunningInstances:
        # for each instance, append to array and print instance id
        ListRunningInstances.append(instance.id)
    return ListRunningInstances

# Print the running instances
def print_running_ec2(RunningInstances):

    for instance in RunningInstances:
        print("[ " + instance.id + " ]")

def ask_user_input1():

    while True:
        terminate_num = int(input("How many do you want tud_cm to dirupt >> [2]: "))
        if  terminate_num==0 or terminate_num > int(original_count):
            print("Please type atleast ""2"" or more to delete any random instances")
        else:
            print("\nThe following {} instance IDs will be disrupted: ".format(terminate_num))
            break
    return terminate_num

def select_random(ListRunningInstances, terminate_num_count):

    random_ec2 = random.choices(ListRunningInstances,k=int(terminate_num_count))

    for random_inst in random_ec2:
        print("[ " + random_inst + " ]")
    return random_ec2



def terminate_ec2(random_ec2):

    #instance_2_id = ec2_re_ob.Instance(random_ec2_2).id
    #print(instance_2_id)
    for term_ec2_id in random_ec2:
        ec2_re_ob.Instance(term_ec2_id).terminate()

    # ec2_re_ob.instances.filter(InstanceIds=ec2_1).terminate()
    # ec2_re_ob.instances.filter(InstanceIds=ec2_2).terminate()



def wait_ec2(original_count):
    # instantiate empty array
    RunningInstances = []

    while True:

        time.sleep(3)
        sys.stdout.write('.')
        sys.stdout.flush()
        # time.sleep(3)
        # print('.', end='', flush=True)


        filters = [
            {
                'Name': 'instance-state-name',
                'Values': ['running']
            }
        ]
        # filter the instances based on filters() above
        #instances = ec2_re_ob.instances.filter(Filters=filters)
        instances = get_ec2_instances()
        for instance in instances:
            # for each instance, append to array

            RunningInstances.append(instance.id)
            check_inst_count = len(RunningInstances)
            #print("check_inst:", check_inst)
            #print("check_id:", RunningInstances)
        check_inst_count = len(RunningInstances)

        #Check the count is back to original count
        #if int(check_inst) != 6
        if int(check_inst_count) != int(original_count):
            RunningInstances = []
            check_inst1 = len(RunningInstances)
            #print(". ")
            if time.time() - start_time > expireTIME:
                return "Failed"
                break
        else:
            #print("A")
            return "Passed"
            break
            # print("[ " + instance.id + " ]")

    print("Time in listing Instances2", time.time() - start_time, "Seconds")

    # for each_in in ec2_re_ob.instances.all():
    #     print("[ "+ each_in.id + " ]")


##########################################################################
        #### MAIN CODE ####
##########################################################################

print("Welcome to TUD Chaos Monkey (tud_cm)\n")

# GET Original running Instances
current_running_ec2 = get_ec2_instances()

# GET Original List of running Instances and place it in list
ec2_list=list_running_ec2(current_running_ec2)

# GET Original Count of Instances:
original_count = get_ec2_running_count(ec2_list)

# Print The running Instances and its count:
print("You current have {} instances running".format(get_ec2_running_count(ec2_list)))
print_running_ec2(current_running_ec2)
# Take input count number
inst_terminate_num = ask_user_input1()

#Make Random instance list from original running ec2 list on user input counts
#select_random_running_machine(*)
random_ec2_list = select_random(ec2_list, inst_terminate_num)

# Print Random selected Instances

print("\n #################### In Main Body now ###############################")
#print("\nThe following {} instance IDs will be disrupted: ",len(random_ec2_list))



print("\nPlease wait while these instances are disrupted ...")

# instance_1_id = ec2_re_ob.Instance(random_ec2_2).id
# instance_2_id = ec2_re_ob.Instance(random_ec2_2).id

### <<<<<<<  TERMINATE >>>>>>>> #####
terminate_ec2(random_ec2_list)

### <<<<<<<  TERMINATE >>>>>>>> #####

# state the status of random instances
# GET update running Instances

running_ec2_after_termination = get_ec2_instances()

instance_count_after_termination = get_ec2_running_count(running_ec2_after_termination)

print("\nYou now have {} instances running after Termination: ".format(instance_count_after_termination))



# GET Original List of running Instances and place it in list
ec2_list_post_term=list_running_ec2(running_ec2_after_termination)
#get_ec2_instances()
print_running_ec2(running_ec2_after_termination)


print("\nNow timing reinstatement... ")
start_time = time.time()
print("\nPlease wait while these AWS HA reinstates the instances ... ")
####OK#####
#====== LONG WAIT =============

testresult=wait_ec2(original_count)






end_time = time.time()
if testresult == "Passed":
    print("\n====tud_cm Test Result====")
    print("\n Test PASSED! It took ", end_time - start_time, " seconds...")

elif testresult == "Failed":
    print("\n====tud_cm Test Result====")
    print("\n Test FAILED! It took ", end_time - start_time, " seconds...")

else:
    print("Something wrong")

print("\n Sending NOTIFICATION now ...")
print ("Ok BYE")
