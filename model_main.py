import sys, time
from model_update_basics import creat_all_tables_not_exist
from model_update_basics import update_security_basic_info
from model_update_finreports import update_bs_all, update_bs_from_file
from model_update_finreports import update_is_all, update_is_from_file
from model_update_finreports import update_cf_all, update_cf_from_file
from model_update_category import update_category_bs, update_category_bs_agg
from model_update_capstruct import update_cap_struct_general_all
from model_update_index import update_all_index_weight

usage_prompt = """
参考命令示例：
python model_main.py create 
python model_main.py update security_basic_info 
python model_main.py update balance_sheet 20000101 20180831 (日期为财报发布日期的起止范围)
python model_main.py update income_statement 20000101 20180831 (日期为财报发布日期的起止范围)
python model_main.py update cash_flow_sheet 20000101 20180831 (日期为财报发布日期的起止范围)
python model_main.py update category_bs (数据源：当前目录下category.xlsx的balance表)
python model_main.py update category_bs_agg (数据源：当前目录下category.xlsx的agg表)
python model_main.py update cap_struct 20000101 20180831 (日期为财报end_date的起止范围，如2018年Q2的财报end_date为20180630)
python model_main.py update index_weight 20180101 20180831（日期为指数权重的交易日）
"""


def isValidDate(date):
	# date的格式为"20180101"，不是"2018-01-01"
	try:
		t = time.strptime(date, '%Y%m%d')
		return True
	except:
		return False


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print('参数不够, ', usage_prompt)
		exit(1)

	task = sys.argv[1]

	if task == 'update' and len(sys.argv) >= 3:
		table = sys.argv[2]
		if table == 'security_basic_info' and len(sys.argv) == 3:
			update_security_basic_info()
		elif table == 'balance_sheet' and len(sys.argv) == 5 and isValidDate(sys.argv[3]) and isValidDate(sys.argv[4]):
			start_date = sys.argv[3]
			end_date = sys.argv[4]
			update_bs_all(start_date, end_date)
		elif table == 'income_statement' and len(sys.argv) == 5 and isValidDate(sys.argv[3]) and isValidDate(sys.argv[4]):
			start_date = sys.argv[3]
			end_date = sys.argv[4]
			update_is_all(start_date, end_date)
		elif table == 'cash_flow_sheet' and len(sys.argv) == 5 and isValidDate(sys.argv[3]) and isValidDate(sys.argv[4]):
			start_date = sys.argv[3]
			end_date = sys.argv[4]
			update_cf_all(start_date, end_date)
		elif table == 'category_bs' and len(sys.argv) == 3:
			update_category_bs()
		elif table == 'category_bs_agg' and len(sys.argv) == 3:
			update_category_bs_agg()
		elif table == 'cap_struct' and len(sys.argv) == 5 and isValidDate(sys.argv[3]) and isValidDate(sys.argv[4]):
			start_date = sys.argv[3]
			end_date = sys.argv[4]
			update_cap_struct_general_all(start_date, end_date)
		elif table == 'index_weight' and len(sys.argv) == 5 and isValidDate(sys.argv[3]) and isValidDate(sys.argv[4]):
			start_date = sys.argv[3]
			end_date = sys.argv[4]
			update_all_index_weight(start_date, end_date)
		else:
			print('参数不正确, ', usage_prompt)
	elif task == 'create' and len(sys.argv) == 2:
		creat_all_tables_not_exist()
	else:
		print('参数不正确, ', usage_prompt)

	exit(1)





# 数据库结构维护：
########################################################

# 1. 创建程序中定义而数据库中未创建的表，不会修改数据库中已有的表
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
# start_date = '20000101'
# end_date = '20180831'
# update_bs_all(start_date, end_date)
# update_bs_from_file('p_ts_code_file.txt', start_date, end_date)


# 更新利润表：income_statement
# start_date = '20000101'
# end_date = '20180831'
# update_is_all(start_date, end_date)
# update_is_from_file('p_ts_code_file.txt', start_date, end_date)


# 更新现金流量表：income_statement
# start_date = '20000101'
# end_date = '20180831'
# update_cf_all(start_date, end_date)
# update_cf_from_file('p_ts_code_file.txt', start_date, end_date)



