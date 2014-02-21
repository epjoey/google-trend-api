from pyGTrends import pyGTrends
connector = pyGTrends('joey@eproject-inc.com', 'tilaivytila77')
connector.download_report(('drought', 'aids', 'obama'))
csv = connector.csv()
o = open( 'report.csv', "wb" )
o.write( csv )