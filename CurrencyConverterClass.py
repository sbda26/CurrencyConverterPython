#!/usr/bin/env python3

import sys # Used for the sys.exit function
import json
import requests
from PyQt5 import QtCore

class CurrencyConverterClass:

  def __init__(self, ui):
    self.__ui = ui
    self.__conversionRatesDictionary = {}
    self.__mostRecentRatesJSON = json.load(open('MostRecentRates.json', encoding="utf-8-sig"))
   

  def Setup(self, sortCurrencies):
    self.__LoadConversionRatesDictionary()
    self.__LoadComboBoxes(sortCurrencies)
    self.__SetCurrencyFromComboBox()
    self.__SetLastUpdateLabel()
    self.__SetEvents()
    # more to follow as necessary
 

 # private functions


  def __LoadConversionRatesDictionary(self):
    # convert tuple to dictionary (https://pynative.com/python-convert-json-string-to-dictionary-not-list/)
    self.__conversionRatesDictionary.clear()
    for key, value in self.__mostRecentRatesJSON['conversion_rates'].items():
      self.__conversionRatesDictionary[key] = value


  def __LoadComboBoxes(self, sortCurrencies):
    self.__ui.cboCurrencyFrom.clear()
    self.__ui.cboCurrencyTo.clear()
    currencies = self.__GetCurrencies(sortCurrencies)
    for currency in currencies:
      self.__ui.cboCurrencyFrom.addItem(currency)
      self.__ui.cboCurrencyTo.addItem(currency)


  def __GetCurrencies(self, sort):
  	if sort == True:
  		return sorted(self.__conversionRatesDictionary.keys())
  	else:
  		return self.__conversionRatesDictionary.keys()


  def __SetCurrencyFromComboBox(self):
  	lastBaseCode = self.__mostRecentRatesJSON['base_code']
  	if lastBaseCode == None:
  		lastBaseCode = "USD"
  	index = self.__ui.cboCurrencyFrom.findText(lastBaseCode, QtCore.Qt.MatchFixedString)
  	self.__ui.cboCurrencyFrom.setCurrentIndex(index)


  def __SetLastUpdateLabel(self):
  	lastUpdate = self.__mostRecentRatesJSON['time_last_update_utc']
  	self.__ui.lblLastConversionRateUpdate.setText(lastUpdate)


  def __SetEvents(self):
    self.__ui.btnConvert.clicked.connect(self.__Convert_Clicked)
    self.__ui.btnUpdate.clicked.connect(self.__Update_Clicked)
    self.__ui.cboCurrencyFrom.currentIndexChanged.connect(self.__CurrencyFrom_Changed)
    # more to follow (btnUpdate)


  def __Convert_Clicked(self):
    baseCode = self.__ui.cboCurrencyFrom.currentText()
    targetCode = self.__ui.cboCurrencyTo.currentText()
    amount = self.__ui.txtAmount.toPlainText()
    baseValue = -1
    try:
      baseValue = float(amount)
    except ValueError:
      baseValue = 0
    conversionRate = float(self.__conversionRatesDictionary[targetCode])
    conversionAmount = float("{:.2f}".format(baseValue * conversionRate))
    self.__ui.lblConversionRate.setText(str(conversionRate))
    self.__ui.lblConvertedAmount.setText(str(conversionAmount))


  def __Update_Clicked(self):
    baseCode = self.__ui.cboCurrencyFrom.currentText()
    # https://www.geeksforgeeks.org/get-post-requests-using-python/
    url = "https://v6.exchangerate-api.com/v6/e462fd853067cde3aff144b6/latest/" + baseCode
    r = requests.get(url = url)
    self.__mostRecentRatesJSON = r.json()
    with open('MostRecentRates.json', 'w') as outfile:
      outfile.write(json.dumps(self.__mostRecentRatesJSON, indent = 4))
      outfile.close()
    self.__LoadConversionRatesDictionary()
    self.__SetLastUpdateLabel()


  def __CurrencyFrom_Changed(self, index):
  	self.__Update_Clicked()
  	# self.__ui.lblLastConversionRateUpdate_Header.setText("CCF CHANGED")














