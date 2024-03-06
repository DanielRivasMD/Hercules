####################################################################################################

def page_turner():

  # iterator control
  pagination = browser.find_element_by_class_name('pagination')

  input_value = "input[value='" + str(ix) + "']"
  turn_page = pagination.find_element_by_css_selector(input_value)
  turn_page.clear()
  turn_page.send_keys((ix + 1))
  turn_page.send_keys(Keys.RETURN)

####################################################################################################
