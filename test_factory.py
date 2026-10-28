import unittest,subprocess,sys,csv,zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class FactoryTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):subprocess.run([sys.executable,str(ROOT/'factory/build.py')],check=True)
 def test_pages(self):
  for name in ['index.html','freelance-rate-calculator.html','privacy.html','style.css','catalog.json']:self.assertTrue((ROOT/'site'/name).stat().st_size>100)
 def test_download(self):
  with zipfile.ZipFile(ROOT/'site/business-template-pack.zip') as z:self.assertEqual(len(z.namelist()),3)
 def test_csv_formulas(self):
  with (ROOT/'products/small-business-cashflow.csv').open() as f:rows=list(csv.reader(f))
  self.assertEqual(len(rows),13);self.assertEqual(rows[1][-1],'=B2+C2+D2-SUM(E2:I2)')
if __name__=='__main__':unittest.main()
