"""'test'

Revision ID: 05c7546d1394
Revises: 54efb785316f
Create Date: 2018-09-16 17:34:19.861568

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '05c7546d1394'
down_revision = '54efb785316f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test_2',
    sa.Column('ts_code', sa.String(length=20), nullable=False),
    sa.Column('symbol', sa.String(length=20), nullable=True),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('fullname', sa.String(length=200), nullable=True),
    sa.Column('enname', sa.String(length=500), nullable=True),
    sa.Column('exchange_id', sa.String(length=20), nullable=True),
    sa.Column('curr_type', sa.String(length=20), nullable=True),
    sa.Column('list_status', sa.String(length=20), nullable=True),
    sa.Column('list_date', sa.String(length=20), nullable=True),
    sa.Column('delist_date', sa.String(length=20), nullable=True),
    sa.Column('is_hs', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('ts_code')
    )
    op.drop_table('income_statement')
    op.drop_table('security_basic_info')
    op.drop_table('balane_sheet')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('balane_sheet',
    sa.Column('ts_code', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('ann_date', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('f_ann_date', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('end_date', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('report_type', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('comp_type', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('total_share', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('cap_rese', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('undistr_porfit', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('surplus_rese', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('special_rese', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('money_cap', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('trad_asset', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('notes_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('accounts_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('prepayment', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('div_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('int_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('inventories', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('amor_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('nca_within_1y', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('sett_rsrv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('loanto_oth_bank_fi', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('premium_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reinsur_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reinsur_res_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('pur_resale_fa', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_cur_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_cur_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('fa_avail_for_sale', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('htm_invest', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('lt_eqt_invest', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('invest_real_estate', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('time_deposits', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('lt_rec', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('fix_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('cip', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('const_materials', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('fixed_assets_disp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('produc_bio_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oil_and_gas_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('intan_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('r_and_d', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('goodwill', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('lt_amor_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('defer_tax_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('decr_in_disbur', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_nca', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_nca', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('cash_reser_cb', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('depos_in_oth_bfi', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('prec_metals', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('deriv_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('rr_reins_une_prem', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('rr_reins_outstd_cla', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('rr_reins_lins_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('rr_reins_lthins_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('refund_depos', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('ph_pledge_loans', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('refund_cap_depos', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('indep_acct_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('client_depos', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('client_prov', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('transac_seat_fee', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('invest_as_receiv', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('lt_borr', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('st_borr', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('cb_borr', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('depos_ib_deposits', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('loan_oth_bank', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('trading_fl', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('notes_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('acct_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('adv_receipts', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('sold_for_repur_fa', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('comm_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('payroll_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('taxes_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('int_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('div_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('acc_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('deferred_inc', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('st_bonds_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('payable_to_reinsurer', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('rsrv_insur_cont', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('acting_trading_sec', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('acting_uw_sec', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('non_cur_liab_due_1y', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_cur_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_cur_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('bond_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('lt_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('specific_payables', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('estimated_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('defer_tax_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('defer_inc_non_cur_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_ncl', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_ncl', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('depos_oth_bfi', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('deriv_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('depos', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('agency_bus_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('prem_receiv_adva', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('depos_received', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('ph_invest', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reser_une_prem', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reser_outstd_claims', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reser_lins_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reser_lthins_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('indept_acc_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('pledge_borr', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('indem_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('policy_div_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('treasury_share', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('ordin_risk_reser', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('forex_differ', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('invest_loss_unconf', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('minority_int', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_hldr_eqy_exc_min_int', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_hldr_eqy_inc_min_int', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_liab_hldr_eqy', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('lt_payroll_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_comp_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_eqt_tools', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_eqt_tools_p_shr', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('lending_funds', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('acc_receivable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('st_fin_payable', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('payables', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('hfs_assets', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('hfs_sales', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.PrimaryKeyConstraint('ts_code', 'ann_date', 'f_ann_date', 'end_date', 'report_type'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('security_basic_info',
    sa.Column('ts_code', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('symbol', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('name', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('fullname', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('enname', mysql.VARCHAR(length=500), nullable=True),
    sa.Column('exchange_id', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('curr_type', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('list_status', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('list_date', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('delist_date', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('is_hs', mysql.VARCHAR(length=20), nullable=True),
    sa.PrimaryKeyConstraint('ts_code'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.create_table('income_statement',
    sa.Column('ts_code', mysql.VARCHAR(length=20), nullable=False),
    sa.Column('ann_date', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('f_ann_date', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('end_date', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('report_type', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('comp_type', mysql.VARCHAR(length=20), nullable=True),
    sa.Column('basic_eps', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('diluted_eps', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_revenue', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('revenue', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('int_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('prem_earned', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('comm_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('n_commis_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('n_oth_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('n_oth_b_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('prem_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('out_prem', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('une_prem_reser', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reins_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('n_sec_tb_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('n_sec_uw_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('n_asset_mg_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_b_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('fv_value_chg_gain', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('invest_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('ass_invest_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('forex_gain', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_cogs', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oper_cost', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('int_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('comm_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('biz_tax_surchg', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('sell_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('admin_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('fin_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('assets_impair_loss', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('prem_refund', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('compens_payout', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reser_insur_liab', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('div_payt', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reins_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oper_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('compens_payout_refu', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('insur_reser_refu', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('reins_cost_refund', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('other_bus_cost', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('operate_profit', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('non_oper_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('non_oper_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('nca_disploss', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('total_profit', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('income_tax', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('n_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('n_income_attr_p', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('minority_gain', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('oth_compr_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('t_compr_income', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('compr_inc_attr_p', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('compr_inc_attr_m_s', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('ebit', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('ebitda', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('insurance_exp', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('undist_profit', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('distable_profit', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.PrimaryKeyConstraint('ts_code'),
    mysql_default_charset='utf8',
    mysql_engine='InnoDB'
    )
    op.drop_table('test_2')
    # ### end Alembic commands ###
