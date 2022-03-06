import pandas as pd
import os

def get_oneday_data(machine_path, machine_id, day):
    data = pd.read_csv(machine_path, header=None)
    # print(data.shape)
    cols = ["k"+str(i) for i in range(data.shape[1])]
    data.columns = cols
    start_index = (day-1)*point_interval + 1 #加1是因为原数据多了一个点只取最后一天的96个点 
    end_index = start_index + point_interval
    day_data = data.iloc[start_index:end_index, :]
    print('save', machine_id, day_data.shape)
    # print(day_data)
    save_path = os.path.join('./54machines_day8', str(machine_id)+'.csv')
    day_data.to_csv(save_path, index=None)

def get_curve(machine_path, machine_id):
    data = pd.read_csv(machine_path)
    col_name = [column for column in data]
    print(col_name)
    for col in col_name:
        value = data[col].tolist()
        timestamp = data.index.tolist()
        data_dic = {'timestamp': timestamp, 'value': value}
        # data_dic = {'value': value}
        kpi_data = pd.DataFrame(data_dic)
        print('save', str(machine_id)+'_'+col, kpi_data.shape)
        save_path = os.path.join('./curves', str(machine_id) + '_' + col + '.csv')
        kpi_data.to_csv(save_path, index=None)
        # kpi_data.to_csv(save_path, index=None, header=None)


if __name__ == '__main__':
    ###将0-199台机器第35天的数据写入到54machines_day8文件夹
    point_interval = 96
    PATH = '.'
    raw_data_path = os.path.join(PATH, 'YiDong_train_detect_txtData')
    machines = os.listdir(raw_data_path)
    print(machines)
    for i, machine in enumerate(machines):
        machine_id = machine[0:-4]
        machine_id_int = int(machine_id)
        if (machine_id_int >= 54):
            continue
        print(i, machine_id_int, type(machine_id_int))
        machine_path = os.path.join(raw_data_path, machine)
        get_oneday_data(machine_path, machine_id_int, 8)

    #将54machines_day8文件夹里的每一条kpi变成一条曲线csv文件存入curves文件夹
    PATH = '.'
    raw_data_path = os.path.join(PATH, '54machines_day8')
    machines = os.listdir(raw_data_path)
    print(machines)
    for i, machine in enumerate(machines):
        machine_id = machine[0:-4]
        machine_id_int = int(machine_id)
        if (machine_id_int >= 54):
            continue
        print(i, machine_id_int, type(machine_id_int))
        machine_path = os.path.join(raw_data_path, machine)
        get_curve(machine_path, machine_id_int)