from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

engine = create_engine('mysql+pymysql://root:orange@localhost:3306/equity', echo=False)
Base = declarative_base()

class SecurityBasicInfo(Base):
	__tablename__ = 'security_basic_info'

	ts_code = Column(String(20), primary_key=True)	# TS股票代码
	symbol = Column(String(20))	# 股票代码
	name = Column(String(50))	# 股票名称
	fullname = Column(String(200)) # 股票全称 
	enname = Column(String(500))	# 英文全称
	exchange_id = Column(String(20))	# 交易所代码  
	curr_type = Column(String(20))	# 交易货币
	list_status = Column(String(20))	# 上市状态 L上市 D退市 P暂停上市
	list_date = Column(String(20))	# 上市日期
	delist_date = Column(String(20))	# 退市日期
	is_hs = Column(String(20))	# 是否沪深港通标的，N否 H沪股通 S深股通

class  BalanceSheet(Base):
	__tablename__ = 'balance_sheet'

	ts_code = Column(String(20), primary_key=True) # TS股票代码
	ann_date = Column(String(20), primary_key=True) # 公告日期，note：首次公告日期
	f_ann_date = Column(String(20), primary_key=True) # 实际公告日期，note：最后一次公告日期，有些报告会修改几版，比如因为首次公告内容有错误
	end_date = Column(String(20), primary_key=True) # 报告期
	report_type = Column(String(20), primary_key=True) # 报表类型：见下方详细说明，1代表合并报表
	comp_type = Column(String(20)) # 公司类型：1一般工商业 2银行 3保险 4证券
	total_share = Column(Float(30))	# 期末总股本
	cap_rese = Column(Float(30))	# 资本公积金
	undistr_porfit = Column(Float(30))	# 未分配利润
	surplus_rese = Column(Float(30))	# 盈余公积金
	special_rese = Column(Float(30))	# 专项储备
	money_cap = Column(Float(30))	# 货币资金
	trad_asset = Column(Float(30))	# 交易性金融资产
	notes_receiv = Column(Float(30))	# 应收票据
	accounts_receiv = Column(Float(30))	# 应收账款
	oth_receiv = Column(Float(30))	# 其他应收款
	prepayment = Column(Float(30))	# 预付款项
	div_receiv = Column(Float(30))	# 应收股利
	int_receiv = Column(Float(30))	# 应收利息
	inventories = Column(Float(30))	# 存货
	amor_exp = Column(Float(30))	# 长期待摊费用
	nca_within_1y = Column(Float(30))	# 一年内到期的非流动资产
	sett_rsrv = Column(Float(30))	# 结算备付金
	loanto_oth_bank_fi = Column(Float(30))	# 拆出资金
	premium_receiv = Column(Float(30))	# 应收保费
	reinsur_receiv = Column(Float(30))	# 应收分保账款
	reinsur_res_receiv = Column(Float(30))	# 应收分保合同准备金
	pur_resale_fa = Column(Float(30))	# 买入返售金融资产
	oth_cur_assets = Column(Float(30))	# 其他流动资产
	total_cur_assets = Column(Float(30))	# 流动资产合计
	fa_avail_for_sale = Column(Float(30))	# 可供出售金融资产
	htm_invest = Column(Float(30))	# 持有至到期投资
	lt_eqt_invest = Column(Float(30))	# 长期股权投资
	invest_real_estate = Column(Float(30))	# 投资性房地产
	time_deposits = Column(Float(30))	# 定期存款
	oth_assets = Column(Float(30))	# 其他资产
	lt_rec = Column(Float(30))	# 长期应收款
	fix_assets = Column(Float(30))	# 固定资产
	cip = Column(Float(30))	# 在建工程
	const_materials = Column(Float(30))	# 工程物资
	fixed_assets_disp = Column(Float(30))	# 固定资产清理
	produc_bio_assets = Column(Float(30))	# 生产性生物资产
	oil_and_gas_assets = Column(Float(30))	# 油气资产
	intan_assets = Column(Float(30))	# 无形资产
	r_and_d = Column(Float(30))	# 研发支出
	goodwill = Column(Float(30))	# 商誉
	lt_amor_exp = Column(Float(30))	# 长期待摊费用
	defer_tax_assets = Column(Float(30))	# 递延所得税资产
	decr_in_disbur = Column(Float(30))	# 发放贷款及垫款
	oth_nca = Column(Float(30))	# 其他非流动资产
	total_nca = Column(Float(30))	# 非流动资产合计
	cash_reser_cb = Column(Float(30))	# 现金及存放中央银行款项
	depos_in_oth_bfi = Column(Float(30))	# 存放同业和其它金融机构款项
	prec_metals = Column(Float(30))	# 贵金属
	deriv_assets = Column(Float(30))	# 衍生金融资产
	rr_reins_une_prem = Column(Float(30))	# 应收分保未到期责任准备金
	rr_reins_outstd_cla = Column(Float(30))	# 应收分保未决赔款准备金
	rr_reins_lins_liab = Column(Float(30))	# 应收分保寿险责任准备金
	rr_reins_lthins_liab = Column(Float(30))	# 应收分保长期健康险责任准备金
	refund_depos = Column(Float(30))	# 存出保证金
	ph_pledge_loans = Column(Float(30))	# 保户质押贷款
	refund_cap_depos = Column(Float(30))	# 存出资本保证金
	indep_acct_assets = Column(Float(30))	# 独立账户资产
	client_depos = Column(Float(30))	# 其中：客户资金存款
	client_prov = Column(Float(30))	# 其中：客户备付金
	transac_seat_fee = Column(Float(30))	# 其中:交易席位费
	invest_as_receiv = Column(Float(30))	# 应收款项类投资
	total_assets = Column(Float(30))	# 资产总计
	lt_borr = Column(Float(30))	# 长期借款
	st_borr = Column(Float(30))	# 短期借款
	cb_borr = Column(Float(30))	# 向中央银行借款
	depos_ib_deposits = Column(Float(30))	# 吸收存款及同业存放
	loan_oth_bank = Column(Float(30))	# 拆入资金
	trading_fl = Column(Float(30))	# 交易性金融负债
	notes_payable = Column(Float(30))	# 应付票据
	acct_payable = Column(Float(30))	# 应付账款
	adv_receipts = Column(Float(30))	# 预收款项
	sold_for_repur_fa = Column(Float(30))	# 卖出回购金融资产款
	comm_payable = Column(Float(30))	# 应付手续费及佣金
	payroll_payable = Column(Float(30))	# 应付职工薪酬
	taxes_payable = Column(Float(30))	# 应交税费
	int_payable = Column(Float(30))	# 应付利息
	div_payable = Column(Float(30))	# 应付股利
	oth_payable = Column(Float(30))	# 其他应付款
	acc_exp = Column(Float(30))	# 预提费用
	deferred_inc = Column(Float(30))	# 递延收益
	st_bonds_payable = Column(Float(30))	# 应付短期债券
	payable_to_reinsurer = Column(Float(30))	# 应付分保账款
	rsrv_insur_cont = Column(Float(30))	# 保险合同准备金
	acting_trading_sec = Column(Float(30))	# 代理买卖证券款
	acting_uw_sec = Column(Float(30))	# 代理承销证券款
	non_cur_liab_due_1y = Column(Float(30))	# 一年内到期的非流动负债
	oth_cur_liab = Column(Float(30))	# 其他流动负债
	total_cur_liab = Column(Float(30))	# 流动负债合计
	bond_payable = Column(Float(30))	# 应付债券
	lt_payable = Column(Float(30))	# 长期应付款
	specific_payables = Column(Float(30))	# 专项应付款
	estimated_liab = Column(Float(30))	# 预计负债
	defer_tax_liab = Column(Float(30))	# 递延所得税负债
	defer_inc_non_cur_liab = Column(Float(30))	# 递延收益-非流动负债
	oth_ncl = Column(Float(30))	# 其他非流动负债
	total_ncl = Column(Float(30))	# 非流动负债合计
	depos_oth_bfi = Column(Float(30))	# 同业和其它金融机构存放款项
	deriv_liab = Column(Float(30))	# 衍生金融负债
	depos = Column(Float(30))	# 吸收存款
	agency_bus_liab = Column(Float(30))	# 代理业务负债
	oth_liab = Column(Float(30))	# 其他负债
	prem_receiv_adva = Column(Float(30))	# 预收保费
	depos_received = Column(Float(30))	# 存入保证金
	ph_invest = Column(Float(30))	# 保户储金及投资款
	reser_une_prem = Column(Float(30))	# 未到期责任准备金
	reser_outstd_claims = Column(Float(30))	# 未决赔款准备金
	reser_lins_liab = Column(Float(30))	# 寿险责任准备金
	reser_lthins_liab = Column(Float(30))	# 长期健康险责任准备金
	indept_acc_liab = Column(Float(30))	# 长期健康险责任准备金
	pledge_borr = Column(Float(30))	# 其中:质押借款
	indem_payable = Column(Float(30))	# 应付赔付款
	policy_div_payable = Column(Float(30))	# 应付保单红利
	total_liab = Column(Float(30))	# 负债合计
	treasury_share = Column(Float(30))	# 减:库存股
	ordin_risk_reser = Column(Float(30))	# 一般风险准备
	forex_differ = Column(Float(30))	# 外币报表折算差额
	invest_loss_unconf = Column(Float(30))	# 未确认的投资损失
	minority_int = Column(Float(30))	# 少数股东权益
	total_hldr_eqy_exc_min_int = Column(Float(30))	# 股东权益合计(不含少数股东权益)
	total_hldr_eqy_inc_min_int = Column(Float(30))	# 股东权益合计(含少数股东权益)
	total_liab_hldr_eqy = Column(Float(30))	# 负债及股东权益总计
	lt_payroll_payable = Column(Float(30))	# 长期应付职工薪酬
	oth_comp_income = Column(Float(30))	# 其他综合收益
	oth_eqt_tools = Column(Float(30))	# 其他权益工具
	oth_eqt_tools_p_shr = Column(Float(30))	# 其他权益工具(优先股)
	lending_funds = Column(Float(30))	# 融出资金
	acc_receivable = Column(Float(30))	# 应收款项
	st_fin_payable = Column(Float(30))	# 应付短期融资款
	payables = Column(Float(30))	# 应付款项
	hfs_assets = Column(Float(30))	# 持有待售的资产
	hfs_sales = Column(Float(30))	# 持有待售的负债


class IncomeStatement(Base):
	__tablename__ = 'income_statement'

	ts_code = Column(String(20), primary_key=True)	# TS股票代码
	ann_date = Column(String(20), primary_key=True)	# 公告日期
	f_ann_date = Column(String(20), primary_key=True)	# 实际公告日期，即发生过数据变更的最终日期
	end_date = Column(String(20), primary_key=True)	# 报告期
	report_type = Column(String(20), primary_key=True)	# 报告类型： 参考下表说明
	comp_type = Column(String(20))	# 公司类型：1一般工商业 2银行 3保险 4证券
	basic_eps = Column(Float(30))	# 基本每股收益
	diluted_eps = Column(Float(30))	# 稀释每股收益
	total_revenue = Column(Float(30))	# 营业总收入
	revenue = Column(Float(30))	# 营业收入
	int_income = Column(Float(30))	# 利息收入
	prem_earned = Column(Float(30))	# 已赚保费
	comm_income = Column(Float(30))	# 手续费及佣金收入
	n_commis_income = Column(Float(30))	# 手续费及佣金净收入
	n_oth_income = Column(Float(30))	# 其他经营净收益
	n_oth_b_income = Column(Float(30))	# 加:其他业务净收益
	prem_income = Column(Float(30))	# 保险业务收入
	out_prem = Column(Float(30))	# 减:分出保费
	une_prem_reser = Column(Float(30))	# 提取未到期责任准备金
	reins_income = Column(Float(30))	# 其中:分保费收入
	n_sec_tb_income = Column(Float(30))	# 代理买卖证券业务净收入
	n_sec_uw_income = Column(Float(30))	# 证券承销业务净收入
	n_asset_mg_income = Column(Float(30))	# 受托客户资产管理业务净收入
	oth_b_income = Column(Float(30))	# 其他业务收入
	fv_value_chg_gain = Column(Float(30))	# 加:公允价值变动净收益
	invest_income = Column(Float(30))	# 加:投资净收益
	ass_invest_income = Column(Float(30))	# 其中:对联营企业和合营企业的投资收益
	forex_gain = Column(Float(30))	# 加:汇兑净收益
	total_cogs = Column(Float(30))	# 营业总成本
	oper_cost = Column(Float(30))	# 减:营业成本
	int_exp = Column(Float(30))	# 减:利息支出
	comm_exp = Column(Float(30))	# 减:手续费及佣金支出
	biz_tax_surchg = Column(Float(30))	# 减:营业税金及附加
	sell_exp = Column(Float(30))	# 减:销售费用
	admin_exp = Column(Float(30))	# 减:管理费用
	fin_exp = Column(Float(30))	# 减:财务费用
	assets_impair_loss = Column(Float(30))	# 减:资产减值损失
	prem_refund = Column(Float(30))	# 退保金
	compens_payout = Column(Float(30))	# 赔付总支出
	reser_insur_liab = Column(Float(30))	# 提取保险责任准备金
	div_payt = Column(Float(30))	# 保户红利支出
	reins_exp = Column(Float(30))	# 分保费用
	oper_exp = Column(Float(30))	# 营业支出
	compens_payout_refu = Column(Float(30))	# 减:摊回赔付支出
	insur_reser_refu = Column(Float(30))	# 减:摊回保险责任准备金
	reins_cost_refund = Column(Float(30))	# 减:摊回分保费用
	other_bus_cost = Column(Float(30))	# 其他业务成本
	operate_profit = Column(Float(30))	# 营业利润
	non_oper_income = Column(Float(30))	# 加:营业外收入
	non_oper_exp = Column(Float(30))	# 减:营业外支出
	nca_disploss = Column(Float(30))	# 其中:减:非流动资产处置净损失
	total_profit = Column(Float(30))	# 利润总额
	income_tax = Column(Float(30))	# 所得税费用
	n_income = Column(Float(30))	# 净利润(含少数股东损益)
	n_income_attr_p = Column(Float(30))	# 净利润(不含少数股东损益)
	minority_gain = Column(Float(30))	# 少数股东损益
	oth_compr_income = Column(Float(30))	# 其他综合收益
	t_compr_income = Column(Float(30))	# 综合收益总额
	compr_inc_attr_p = Column(Float(30))	# 归属于母公司(或股东)的综合收益总额
	compr_inc_attr_m_s = Column(Float(30))	# 归属于少数股东的综合收益总额
	ebit = Column(Float(30))	# 息税前利润
	ebitda = Column(Float(30))	# 息税折旧摊销前利润
	insurance_exp = Column(Float(30))	# 保险业务支出
	undist_profit = Column(Float(30))	# 年初未分配利润
	distable_profit = Column(Float(30))	# 可分配利润


class CashFlowSheet(Base):
	__tablename__ = 'cash_flow_sheet'

	ts_code = Column(String(20), primary_key=True)	# TS股票代码
	ann_date = Column(String(20), primary_key=True)	# 公告日期
	f_ann_date = Column(String(20), primary_key=True)	# 实际公告日期
	end_date = Column(String(20), primary_key=True)	# 报告期
	comp_type = Column(String(20))	# 公司类型：1一般工商业 2银行 3保险 4证券
	report_type = Column(String(20), primary_key=True)	# 报表类型：见下方详细说明
	net_profit = Column(Float(30))	# 净利润
	finan_exp = Column(Float(30))	# 财务费用
	c_fr_sale_sg = Column(Float(30))	# 销售商品、提供劳务收到的现金
	recp_tax_rends = Column(Float(30))	# 收到的税费返还
	n_depos_incr_fi = Column(Float(30))	# 客户存款和同业存放款项净增加额
	n_incr_loans_cb = Column(Float(30))	# 向中央银行借款净增加额
	n_inc_borr_oth_fi = Column(Float(30))	# 向其他金融机构拆入资金净增加额
	prem_fr_orig_contr = Column(Float(30))	# 收到原保险合同保费取得的现金
	n_incr_insured_dep = Column(Float(30))	# 保户储金净增加额
	n_reinsur_prem = Column(Float(30))	# 收到再保业务现金净额
	n_incr_disp_tfa = Column(Float(30))	# 处置交易性金融资产净增加额
	ifc_cash_incr = Column(Float(30))	# 收取利息和手续费净增加额
	n_incr_disp_faas = Column(Float(30))	# 处置可供出售金融资产净增加额
	n_incr_loans_oth_bank = Column(Float(30))	# 拆入资金净增加额
	n_cap_incr_repur = Column(Float(30))	# 回购业务资金净增加额
	c_fr_oth_operate_a = Column(Float(30))	# 收到其他与经营活动有关的现金
	c_inf_fr_operate_a = Column(Float(30))	# 经营活动现金流入小计
	c_paid_goods_s = Column(Float(30))	# 购买商品、接受劳务支付的现金
	c_paid_to_for_empl = Column(Float(30))	# 支付给职工以及为职工支付的现金
	c_paid_for_taxes = Column(Float(30))	# 支付的各项税费
	n_incr_clt_loan_adv = Column(Float(30))	# 客户贷款及垫款净增加额
	n_incr_dep_cbob = Column(Float(30))	# 存放央行和同业款项净增加额
	c_pay_claims_orig_inco = Column(Float(30))	# 支付原保险合同赔付款项的现金
	pay_handling_chrg = Column(Float(30))	# 支付手续费的现金
	pay_comm_insur_plcy = Column(Float(30))	# 支付保单红利的现金
	oth_cash_pay_oper_act = Column(Float(30))	# 支付其他与经营活动有关的现金
	st_cash_out_act = Column(Float(30))	# 经营活动现金流出小计
	n_cashflow_act = Column(Float(30))	# 经营活动产生的现金流量净额
	oth_recp_ral_inv_act = Column(Float(30))	# 收到其他与投资活动有关的现金
	c_disp_withdrwl_invest = Column(Float(30))	# 收回投资收到的现金
	c_recp_return_invest = Column(Float(30))	# 取得投资收益收到的现金
	n_recp_disp_fiolta = Column(Float(30))	# 处置固定资产、无形资产和其他长期资产收回的现金净额
	n_recp_disp_sobu = Column(Float(30))	# 处置子公司及其他营业单位收到的现金净额
	stot_inflows_inv_act = Column(Float(30))	# 投资活动现金流入小计
	c_pay_acq_const_fiolta = Column(Float(30))	# 购建固定资产、无形资产和其他长期资产支付的现金
	c_paid_invest = Column(Float(30))	# 投资支付的现金
	n_disp_subs_oth_biz = Column(Float(30))	# 取得子公司及其他营业单位支付的现金净额
	oth_pay_ral_inv_act = Column(Float(30))	# 支付其他与投资活动有关的现金
	n_incr_pledge_loan = Column(Float(30))	# 质押贷款净增加额
	stot_out_inv_act = Column(Float(30))	# 投资活动现金流出小计
	n_cashflow_inv_act = Column(Float(30))	# 投资活动产生的现金流量净额
	c_recp_borrow = Column(Float(30))	# 取得借款收到的现金
	proc_issue_bonds = Column(Float(30))	# 发行债券收到的现金
	oth_cash_recp_ral_fnc_act = Column(Float(30))	# 收到其他与筹资活动有关的现金
	stot_cash_in_fnc_act = Column(Float(30))	# 筹资活动现金流入小计
	free_cashflow = Column(Float(30))	# 企业自由现金流量
	c_prepay_amt_borr = Column(Float(30))	# 偿还债务支付的现金
	c_pay_dist_dpcp_int_exp = Column(Float(30))	# 分配股利、利润或偿付利息支付的现金
	incl_dvd_profit_paid_sc_ms = Column(Float(30))	# 其中:子公司支付给少数股东的股利、利润
	oth_cashpay_ral_fnc_act = Column(Float(30))	# 支付其他与筹资活动有关的现金
	stot_cashout_fnc_act = Column(Float(30))	# 筹资活动现金流出小计
	n_cash_flows_fnc_act = Column(Float(30))	# 筹资活动产生的现金流量净额
	eff_fx_flu_cash = Column(Float(30))	# 汇率变动对现金的影响
	n_incr_cash_cash_equ = Column(Float(30))	# 现金及现金等价物净增加额
	c_cash_equ_beg_period = Column(Float(30))	# 期初现金及现金等价物余额
	c_cash_equ_end_period = Column(Float(30))	# 期末现金及现金等价物余额
	c_recp_cap_contrib = Column(Float(30))	# 吸收投资收到的现金
	incl_cash_rec_saims = Column(Float(30))	# 其中:子公司吸收少数股东投资收到的现金
	uncon_invest_loss = Column(Float(30))	# 未确认投资损失
	prov_depr_assets = Column(Float(30))	# 加:资产减值准备
	depr_fa_coga_dpba = Column(Float(30))	# 固定资产折旧、油气资产折耗、生产性生物资产折旧
	amort_intang_assets = Column(Float(30))	# 无形资产摊销
	lt_amort_deferred_exp = Column(Float(30))	# 长期待摊费用摊销
	decr_deferred_exp = Column(Float(30))	# 待摊费用减少
	incr_acc_exp = Column(Float(30))	# 预提费用增加
	loss_disp_fiolta = Column(Float(30))	# 处置固定、无形资产和其他长期资产的损失
	loss_scr_fa = Column(Float(30))	# 固定资产报废损失
	loss_fv_chg = Column(Float(30))	# 公允价值变动损失
	invest_loss = Column(Float(30))	# 投资损失
	decr_def_inc_tax_assets = Column(Float(30))	# 递延所得税资产减少
	incr_def_inc_tax_liab = Column(Float(30))	# 递延所得税负债增加
	decr_inventories = Column(Float(30))	# 存货的减少
	decr_oper_payable = Column(Float(30))	# 经营性应收项目的减少
	incr_oper_payable = Column(Float(30))	# 经营性应付项目的增加
	others = Column(Float(30))	# 其他
	im_net_cashflow_oper_act = Column(Float(30))	# 经营活动产生的现金流量净额(间接法)
	conv_debt_into_cap = Column(Float(30))	# 债务转为资本
	conv_copbonds_due_within_1y = Column(Float(30))	# 一年内到期的可转换公司债券
	fa_fnc_leases = Column(Float(30))	# 融资租入固定资产
	end_bal_cash = Column(Float(30))	# 现金的期末余额
	beg_bal_cash = Column(Float(30))	# 减:现金的期初余额
	end_bal_cash_equ = Column(Float(30))	# 加:现金等价物的期末余额
	beg_bal_cash_equ = Column(Float(30))	# 减:现金等价物的期初余额
	im_n_incr_cash_equ = Column(Float(30))	# 现金及现金等价物净增加额(间接法)

	
# important: 区分__table__和__tablename__，一个是Table()类，一个是表名字符串
# print(SecurityBasicInfo.__table__, type(SecurityBasicInfo.__table__))
# print(SecurityBasicInfo.__tablename__, type(SecurityBasicInfo.__tablename__))
# print(BalanceSheet.__table__.c)

