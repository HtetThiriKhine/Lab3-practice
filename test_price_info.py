import price_info as main

def test_cost_of_fruit():
    fruit = 'apple'
    quantity = 10
    expected_result = 1.20*10
    result= quantity* main.price_list[fruit]
    assert result == expected_result , f"Expected {expected_result}, got{result}"
     
def test_total_cost_shopping():

    expected_cost=0
    for key in main.price_list.keys():
        if key in main.quantity_list:
            expected_cost += main.price_list[key]* main.quantity_list[key]
    

    total_cost = 0
    for key in main.price_list.keys():
        if key in main.quantity_list:
            total_cost += main.price_list[key]* main.quantity_list[key]

    assert total_cost==expected_cost , f"Expected {expected_cost}, got{total_cost}"
    