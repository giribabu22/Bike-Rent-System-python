import time,json,os
# total_bikes_data = {'apache':40,'splendor':150,'pulsar':34,'honda sp ':70,'suzuki gsx':10,'ktm':15,'fzs':25,'fz':25,}

print('welcome to the mintripe')

if os.path.exists('dataBase/total_bikes_data.json'):
  with open('dataBase/total_bikes_data.json') as fi:
      total_bikes_data=json.load(fi)
with open('dataBase/data.json') as f:
      data = json.load(f)
with open('dataBase/total_bikes_data.json') as fi2:
  total_bikes_data=json.load(fi2)
rent_data = {}


class customer_data:
  def send_data_to_json(Self):
    with open('dataBase/data.json','w') as f:
        json.dump(rent_data,f,indent=3)
    with open('dataBase/total_bikes_data.json','w') as fi2:
      json.dump(total_bikes_data,fi2,indent=3)
  def read_data_in_json():
    with open('dataBase/data.json') as f:
      data = json.load(f)
    with open('dataBase/total_bikes_data.json') as fi2:
      total_bikes_data=json.load(fi2)
  read_data_in_json()
  def bik_(Self):
    if os.path.exists('dataBase/data.json'):
      with open('dataBase/data.json') as fi:
        rent_data=json.load(fi)
    x,bike_names_list,prs_data  =  1,[],{}

    name = input('enter the name :')
    if name not in rent_data:
      for i in total_bikes_data.keys():
        bike_names_list.append(i)
        print('\t',x,i)
        x+=1
      wh_bike = int(input('\nenter :'))
      print(bike_names_list[wh_bike-1])
      time_ = time.time()
      while True:
        how_many_bikes = int(input('how many bikes you want :'))
        res = total_bikes_data[bike_names_list[wh_bike-1]]
        if res >= how_many_bikes:
          pno = int(input('enter the phone number :'))
          gnd = input('enter the gender M/F :')
          res2,dic_bik = res - how_many_bikes,{}
          total_bikes_data[bike_names_list[wh_bike-1]] = res2
          bike_data = [time_,how_many_bikes]
          prs_data['userName'],prs_data['mobile_num'],prs_data['gender'],prs_data[bike_names_list[wh_bike-1]] = name,pno,gnd,bike_data
          if gnd == 'f' or gnd == 'F':
            res6='madam'
          else:
            res6 = 'sir'
          print(f'\n{res6}',name,' \nyour number',pno,'you selected bike',bike_names_list[wh_bike-1],'qnt of the bikes',how_many_bikes,'per hour 50rs')
          break
        elif res == 0:
          print('\n this bikes are not avalible')
          break
        else:
          print(f"we don't have this many bakes {how_many_bikes}")
          pass
      rent_data[name] = [prs_data]
      print(rent_data)
    else:
      print('hello',name)
      for i in total_bikes_data.keys():
        bike_names_list.append(i)
        print('\t',x,i)
        x+=1
      wh_bike = int(input('enter :'))
      print(bike_names_list[wh_bike-1])
      li_remove = ['userName','mobile_num','gender']
      for li5 in data[name]:
        for gh in li5:
          if bike_names_list[wh_bike-1] in li_remove:
            print(gh,'@@@@@@@@@@@@@@@@@')
      time_ = time.time()
      while True:
        how_many_bikes = int(input('how many bikes you want :'))
        res = total_bikes_data[bike_names_list[wh_bike-1]]
        if res >= how_many_bikes:
          res2 = res - how_many_bikes
          total_bikes_data[bike_names_list[wh_bike-1]] = res2
          name = [time_,how_many_bikes]
          # prs_data[bike_names_list[wh_bike-1]] = [bike_data]
          print(name,'runnong')
          break
        elif res == 0:
          print('\nthis bikes are not avalible')
          break
        else:
          print(f"we don't have this many bakes {how_many_bikes}")
          pass
      # rent_data[name].append(prs_data)
    c2 = input('enter yes or no :')
    if c2 == 'yes' or c2 == 'y':
      with open('dataBase/data.json','w') as f:
        json.dump(rent_data,f,indent=3)

      with open('dataBase/total_bikes_data.json','w') as fi2:
        json.dump(total_bikes_data,fi2,indent=3)
    else:
      print('\ntry another time')

class return_(customer_data):
  def call_data(self):
    with open('dataBase/data.json') as fl :
      return_data = json.load(fl)
    name = input('enter the name :')
    if name in return_data:
      res1=return_data.get(name)
      z,b_n,b_q=1,[],[]3

      for bike_names_list in res1:
        for k,v in bike_names_list.items():
          if 'bike_name' ==k:
            b_n.append(v)
            print('\t',z,v)
            z+=1
          if 'no_of_bikes' ==k:
            b_q.append(v)
          
      rtn_b = int(input('enter '))-1
      print('no of bikes you taken ',b_q[rtn_b])
      return_bikes = int(input('enter the return bikes :'))
      for d in res1:
        for k,v in d.items():
          if b_n[rtn_b] == v:
            print(d['no_of_bikes'], return_bikes)
            if d['no_of_bikes'] >= return_bikes:
              zxc = return_bikes - d['no_of_bikes']
              d['no_of_bikes'] = zxc
              if zxc == 0:
                print(return_data[name])
                del return_data[name]
      print(return_data)
      rtn_obj.send_data_to_json()

while True:
  print( ' \n 1) rent for bike\n 2) return the bike\n 3) exit \n ')
  c = input('enter :')

  if c == '1':
    bike_obj = customer_data()
    bike_obj.bik_()

  # elif c == '2':
  #   rtn_obj = return_()
  #   rtn_obj.call_data()

  elif c == '3':
    print()

  else:
    print('<<<<< thank you >>>>>')
    break
