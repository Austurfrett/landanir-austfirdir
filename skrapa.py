import json
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        url = "https://island.is/v/gagnasidur-fiskistofu/gagnasidur?pageName=ReportSection442204bd163088050bb0"
        page.goto(url)
        
        try:
            page.wait_for_selector("iframe", timeout=30000)
            rammi = page.frame_locator("iframe").first
            
            rammi.locator("div[role='gridcell']").first.wait_for(timeout=30000)
            
            frumur = rammi.locator("div[role='gridcell']").all_inner_texts()
            
            print(f"Sannprófun: Fann {len(frumur)} frumur.")
            print("Dæmi um gögn:", frumur[:20])
            
        except Exception as e:
            print(f"Gat ekki lesið töflu: {e}")
            
        with open('landanir.json', 'w', encoding='utf-8') as f:
            json.dump([], f, ensure_ascii=False, indent=2)

        browser.close()

if __name__ == '__main__':
    run()
