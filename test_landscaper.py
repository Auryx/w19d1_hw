import landscaper

## Test that start function returns result of input
def test_start():
    print("TESTING THE START FUNCTION")
    landscaper.input = lambda a: "1"
    assert landscaper.start() == "1"

## Test that the selection function when passed one will increased money by 1
def test_selection_mow():
    print("TESTING THE SELECTION AND MOW FUNCTION")
    landscaper.selection("1")
    assert landscaper.money == 1

## Test that upgrade function increments current_tool by 1
def test_selection_upgrade():
    print("TESTING THE SELECTION AND UPGRADE FUNCTION")
    landscaper.money = 5
    landscaper.selection("2")
    assert landscaper.current_tool == 1

## Test win condition works
def test_win_conditions():
    print("TESTING THE WIN CONDITIONS FUNCTION")
    landscaper.money = 1000
    landscaper.current_tool = 4
    assert landscaper.win_conditions() == True