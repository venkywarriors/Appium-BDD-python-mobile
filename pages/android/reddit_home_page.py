import logging
import re
import sys
from time import sleep

from selenium.webdriver.common.by import By
from utils.base_page import BasePage


logger = logging.getLogger('behaving')

class RedditHomePage(BasePage):
    #Reddit home page
    launch_logo_loc          = (By.ID, "com.reddit.frontpage:id/launch_logo")
    welcome_msg_loc          = (By.ID, "com.reddit.frontpage:id/welcome_message")
    login_button_loc         = (By.ID, "com.reddit.frontpage:id/login_button")
    sign_up_button_loc       = (By.ID, "com.reddit.frontpage:id/signup_button")
    skip_login_link_loc      = (By.ID, "com.reddit.frontpage:id/skip_text")

    #Alert message modal
    alert_msg_title_loc      = (By.ID, "com.reddit.frontpage:id/alertTitle")
    alert_msg_yes_button_loc = (By.ID, "android:id/button1")
    alert_msg_no_button_loc  = (By.ID, "android:id/button2")

    #Searched result list
    word_mark_loc            = (By.ID, "com.reddit.frontpage:id/search_mag_icon")
    search_icon_loc          = (By.ID, "com.reddit.frontpage:id/reddit_wordmark")
    search_field_loc         = (By.ID, "com.reddit.frontpage:id/search_src_text")
    search_results_loc       = (By.CLASS_NAME, "android.widget.RelativeLayout")
    search_results_name_loc  = (By.ID, "com.reddit.frontpage:id/subreddit_name")

    #subreddit page
    profile_name_loc         = (By.ID, "com.reddit.frontpage:id/profile_name")
    layout_loc               = (By.CLASS_NAME, "android.widget.LinearLayout")
    link_title_loc           = (By.ID, "com.reddit.frontpage:id/link_title")

    def skip_on_board_page(self):
        if self.is_element_found(*self.skip_login_link_loc) == True:
            self.find_element(*self.skip_login_link_loc).click()
        elif self.is_element_found(*self.search_field_loc) == True:
            pass
        #Sometime  an alert modal pops up
        elif is_alert_modal_displayed(self) == True:
            dismiss_altert_modal(self)
        else:
            self.fail("STDOUT: Can't find on board page. \n")
        return

    def input_searched_term(self, searched_term):
        if self.is_element_found(*self.search_field_loc) == True:
            self.send_keys(searched_term, *self.search_field_loc)
        elif is_alert_modal_displayed(self) == True:
                dismiss_altert_modal(self)
        else:
            self.fail("STDOUT: Can't find search field. \n")
        return

    def check_searched_result_is_displayed(self, searched_term):
        names_array = self.fetch_elements_name(*self.search_results_name_loc)
        if names_array == None:
            self.fail("STDOUT: Can't find searched result: %s. \n" % searched_term)
            return False
        for i in range(names_array.__len__()):
            result_name = names_array[i]
            if  searched_term == result_name[2:]:
                return True
        self.fail("STDOUT: Can't find searched result: %s. \n" % searched_term)
        return False

    def is_alert_modal_displayed(self):
        if self.is_element_found(*self.alert_msg_title_loc) == True:
            return True
        return False

    def dismiss_altert_modal(self):
        self.find_element(*self.alert_msg_yes_button_loc).click()

    def tap_on_the_searched_result(self, searched_term):
        names_array = self.fetch_elements_name(*self.search_results_name_loc)
        if names_array == None:
            self.fail("STDOUT: Can't find searched result: %s. \n" % searched_term)
            return
        for i in range(names_array.__len__()):
            search_result_name = names_array[i]
            if searched_term == search_result_name[2:]:
                if self.find_the_specific_tapable_element(i, *self.search_results_name_loc) != None:
                    self.find_the_specific_tapable_element(i, *self.search_results_name_loc).click()
                    return
        self.fail("STDOUT: Can't tap on the searched result: %s. \n" % searched_term)
        return

    def check_specific_term_in_top_posted_title(self, check_term):
        title_names = self.fetch_elements_name(*self.link_title_loc)
        if title_names == None:
            return False
        if check_term in title_names[0]:
            sys.stdout.write("\n\n Top posted title : \"%s\" contains CHECK TERM : \"%s\". \n\n " % (title_names[0], check_term))
            return True
        sys.stdout.write("\n\n Top posted title : \"%s\" does not contain CHECK TERM : \"%s\". \n\n " % (title_names[0], check_term))
        return False
