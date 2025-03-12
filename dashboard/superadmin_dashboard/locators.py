# New Event
new_event_xpath = '//span[contains(text(), "New Event")]'
add_new_event_id = '#exampleModalLabel'
title_name = "title"
event_start_date_id = "startDate"
check_all_day_css = '[for="all_day"]'
start_time_name = "start_time"
end_time_name = "end_time"
link_id = "#link"
calender_select_id = '#react-select-6-live-region'
description_event_css = '[class="ql-editor ql-blank"]'
button_save_xpath = "//button[contains(text(), 'Add')]"
button_cancel_xpathh = "//button[contains(text(), 'Cancel')]"
error_title_xpath = "//label[contains(text(), 'Title is required')]"
error_end_time_xpath = "//label[text()='End time is required']"
error_calendar_id = "//label[text()='Calendar ID is required']"

# To do


# Roles
all_roles_css = '[class="left-sec d-flex align-items-center gap-1"]'
view_all_roles_xpath = "//h4[contains(text(), 'Roles')]/parent::div/following-sibling::*/span"
back_btn_xpath = '//*[@class="font--14 cursor--pointer view-all" and contains(text(), "Back")]'

# text
txt_dashboard_css = 'a[href="/dashboard"]'
text_side_bar_xpath = '//div[@class="sidebar-menu  w-100 overflow-y-auto d-flex align-items-center  flex-column ' \
                      'gap-1"]//span[string-length(text()) > 0] '
text_all_roles = '[class="left-sec d-flex align-items-center gap-1"]'
headings_text = '[class="text--black font--18 fw--700 mb-0"]'
to_do_txt = "//div/h4[contains(text(), 'To-Do')]"
