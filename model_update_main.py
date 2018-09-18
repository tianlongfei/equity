from model_update import creat_all_tables_not_exist
from model_update import update_security_basic_info
from model_update import update_bs_all, update_bs_from_file
from model_update import update_is_all, update_is_from_file
from model_update import update_cf_all, update_cf_from_file

# 数据库结构维护：
########################################################

# 1. 创建程序中定义而数据库中未创建的表，但不会删除程序中未定义而数据库中已有的表
# creat_all_tables_not_exist()

# 2. 基于Alembic
# 创建程序中定义而数据库中未创建的表，同时删除程序中未定义而数据库中已有的表。删除的表中的数据也会消失，无法恢复。
# 增加程序中定义的列，同时删除程序中未定义的列。删除的列数据也会消失，无法恢复。
# alembic revision --autogenerate -m 'comment'
# alembic upgrade head
# alembic downgrade -1	
# 注意，downgrade只能恢复upgrade之前的tables name和table columns，已经删除的数据不能恢复，所以要保证每次upgrade正确，不能指望downgrade恢复



# 数据更新：
########################################################

# 更新基础数据表：security_basic_info
# update_security_basic_info()


# 更新财务报表：
# 一般操作是：
# step1: 执行下面程序，如遇执行过程中断(手工或其他因素)，再次执行，直到程序正常结束。
# step2: 然后将except_list.txt, 或者from_file_except_list.txt内容拷贝到p_ts_code_file.txt。
# step3：回到step1。

# 更新资产负债表：balance_sheet
# start_date = '20130101'
# end_date = '20151231'
# update_bs_all(start_date, end_date)
# update_bs_from_file('p_ts_code_file.txt', start_date, end_date)


# 更新利润表：income_statement
# start_date = '20130101'
# end_date = '20181231'
# update_is_all(start_date, end_date)
# update_is_from_file('p_ts_code_file.txt', start_date, end_date)


# 更新现金流量表：income_statement
start_date = '20130101'
end_date = '20181231'
# update_cf_all(start_date, end_date)
update_cf_from_file('p_ts_code_file.txt', start_date, end_date)



# 已经更新：balance_sheet，20130101-20180801
# 已经更新：income_statement，20130101-20180801
# 已经更新：cash_flow_sheet，20130101-20180801


