# -*- coding: utf-8 -*-
# Created By: Virgil Dupras
# Created On: 2010-07-27
# Copyright 2010 Hardcoded Software (http://www.hardcoded.net)
# 
# This software is licensed under the "HS" License as described in the "LICENSE" file, 
# which should be included with this package. The terms are also available at 
# http://www.hardcoded.net/licenses/hs_license

from .base import DocumentGUIObject

def column_prop(viewname, tablename, colname):
    def fget(self):
        view = getattr(self.mainwindow, viewname)
        table = getattr(view, tablename)
        return table.columns.column_is_visible(colname)
    
    def fset(self, visible):
        view = getattr(self.mainwindow, viewname)
        table = getattr(view, tablename)
        return table.columns.set_column_visible(colname, visible)
    
    return property(fget, fset)

class ViewOptions(DocumentGUIObject):
    def __init__(self, view, mainwindow):
        DocumentGUIObject.__init__(self, view, mainwindow.document)
        self.mainwindow = mainwindow
    
    networth_sheet_delta = column_prop('nwview', 'bsheet', 'delta')
    networth_sheet_delta_perc = column_prop('nwview', 'bsheet', 'delta_perc')
    networth_sheet_start = column_prop('nwview', 'bsheet', 'start')
    networth_sheet_budgeted = column_prop('nwview', 'bsheet', 'budgeted')
    networth_sheet_account_number = column_prop('nwview', 'bsheet', 'account_number')
    
    profit_sheet_delta = column_prop('pview', 'istatement', 'delta')
    profit_sheet_delta_perc = column_prop('pview', 'istatement', 'delta_perc')
    profit_sheet_last_cash_flow = column_prop('pview', 'istatement', 'last_cash_flow')
    profit_sheet_budgeted = column_prop('pview', 'istatement', 'budgeted')
    profit_sheet_account_number = column_prop('pview', 'istatement', 'account_number')
    
    transaction_table_description = column_prop('tview', 'ttable', 'description')
    transaction_table_payee = column_prop('tview', 'ttable', 'payee')
    transaction_table_checkno = column_prop('tview', 'ttable', 'checkno')
    
    entry_table_description = column_prop('aview', 'etable', 'description')
    entry_table_payee = column_prop('aview', 'etable', 'payee')
    entry_table_checkno = column_prop('aview', 'etable', 'checkno')
    entry_table_reconciliation_date = column_prop('aview', 'etable', 'reconciliation_date')
    
    schedule_table_description = column_prop('scview', 'sctable', 'description')
    schedule_table_payee = column_prop('scview', 'sctable', 'payee')
    schedule_table_checkno = column_prop('scview', 'sctable', 'checkno')
