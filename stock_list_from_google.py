from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


def verify_url_navigation() -> str:
    """Grabs the title of the page and returns the value

    Returns:
        str: Name of the title of the page
    """
    title_name = driver.find_element(by=By.ID, value="sdgBod").text
    return title_name

def get_stock_list_of_interest() -> None:
    """Gets the list of the stocks from google finance website under the
    list of Interested Stocks

    Returns:
        list: Returns the list of interested stock
    """
    text_box = driver.find_elements(by=By.XPATH, value='//div[@class="COaKTb"]')
    total_stocks = []
    for i in text_box:
        total_stocks.append(i.text)

    stocks_of_interest = total_stocks[:6]
    return stocks_of_interest

def stocks_of_interest_not_in_given_data(given_list: list, stock_list_of_interest: list) -> list:
    """Returns the list of stocks present in the list of interested
    stock but not in the given test data

    Args:
        given_list (List): Pre-defined. Given by the user
        stock_list_of_interest (List): List of interested stocks from the Google finance list

    Returns:
       List: Returns a list of stock exclusive to the list of Interested stock data
    """
    return [stock for stock in stock_list_of_interest if stock not in given_list]

def data_stocks_not_in_stocks_of_interest(given_list: list, stock_list_of_interest: list) -> list:
    """Returns the list of stocks present in the given
    test data but not in list of Interested Stocks

    Args:
        given_list (List): Pre-defined. Given by the user
        stock_list_of_interest (List): List of interested stocks from the Google finance list

    Returns:
        List: Returns a list of stock exclusive to the given data
    """
    return [stock for stock in given_list if stock not in stock_list_of_interest]

def main():

    driver.get("https://www.google.com/finance")
    title = driver.title
    driver.implicitly_wait(5)

    given_list = ["NFLX","MSFT", "TSLA"]
    stock_list_of_interest = get_stock_list_of_interest()

    title_name = verify_url_navigation()
    assert title_name == "Finance"

    # STEP: Comparing the stock
    print("From the given test data: ",given_list)
    print("From the today list of interested stock: ",stock_list_of_interest)

    # STEP: Stocks exclusive to "Stocks of Interest" only
    exclusive_stocks_of_interest = stocks_of_interest_not_in_given_data(given_list, stock_list_of_interest)
    print("\nList of interested stocks not in given data: ",exclusive_stocks_of_interest)

    # STEP: Stocks exclusive to given data only
    exclusive_given_data_stocks = data_stocks_not_in_stocks_of_interest(given_list, stock_list_of_interest)
    print("List of stocks in given data only (Not present in list of interested stocks): ",exclusive_given_data_stocks)


main()

"""
-------OUTPUT-------
From the given test data:  ['NFLX', 'MSFT', 'TSLA']
From the today list of interested stock:  ['NXST', 'BA', 'TSLA', 'BABA', 'AAPL', 'INDEX']

List of interested stocks not in given data:  ['NXST', 'BA', 'BABA', 'AAPL', 'INDEX']
List of stocks in given data only (Not present in list of interested stocks):  ['NFLX', 'MSFT']
"""
