name: Sækja landanir

on:
  schedule:
    - cron: '0 */3 * * *'
  workflow_dispatch:

env:
  FORCE_JAVASCRIPT_ACTIONS_TO_NODE24: true

jobs:
  skrapa:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      
      - name: Setja upp Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
          
      - name: Setja inn pakka
        run: pip install requests beautifulsoup4
        
      - name: Keyra skröpun
        run: python skrapa.py
        
      - name: Vista ný gögn í geymslu
        run: |
          git config --local user.email "action@github.com"
          git config --local user.name "GitHub Action"
          git pull origin main --rebase
          git add landanir.json
          git diff --quiet && git diff --staged --quiet || (git commit -m "Uppfæra landanir" && git push)
