class SwapPageElements:
    open_chains = "//div[contains(text(),'Ethereum')]"
    btn_swap = "//*[text()='Swap']"
    btn_advance_setting = "//button[@id='open-settings-dialog-button' and @aria-label ='Transaction Settings']"
    title_advance_setting = "//div[contains(text(),'Advanced Settings')]"
    slippage_text_field = "//body/div[@id='root']/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[" \
                          "2]/span[1]/div[1]/div[2]/div[1]/div[1]/div[2]/button[4]/div[1]/input[1] "
    btn_more_information = "//div[contains(text(),'MORE INFORMATION')]"
    minimum_received_value = "//html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/div[" \
                             "1]/div[3]/div[2]/div[1] "
    gas_fee_value = "//html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/div[1]/div[" \
                    "4]/div[2] "
    price_impact_value = "//html[1]/body[1]/div[1]/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[3]/div[1]/div[" \
                         "1]/div[5]/div[2]"
    amount_in = "#swap-currency-input .token-amount-input"
    amount_out = "#swap-currency-output .token-amount-input"
    currency_input = "//body/div[@id='root']/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[1]/div[" \
                     "2]/div[1]/div[2]/button[1]/span[1] "
    current_output = "//body/div[@id='root']/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[3]/div[" \
                     "1]/div[2]/div[1]/div[2]/button[1]/span[1]/span[1] "
    slippage_value = "//body/div[@id='root']/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[2]/div[1]/div[4]/div[" \
                     "1]/div[2]/div[1] "
    transaction_time_limit_field = "//body/div[@id='root']/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[" \
                                   "2]/div[1]/div[2]/span[1]/div[1]/div[2]/div[1]/div[2]/div[2]/button[1]/input[1] "
    btn_advance_config = "//button[@id='toggle-expert-mode-button']"
    advance_mode_on = "//body/div[@id='root']/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[" \
                      "2]/span[1]/div[1]/div[2]/div[2]/button[1]/span[1] "
    advance_mode_off = "//body/div[@id='root']/div[1]/div[2]/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[" \
                       "2]/span[1]/div[1]/div[2]/div[2]/button[1]/span[2] "
    advance_mode_term = " //body/reach-portal[9]/div[3]/div[1]/div[1]/div[1]/div[1]/div[2]"
    advance_mode_term_1 = "//div[@class='css-1pxm4lx']"
    btn_cancel = "//button[contains(text(),'Cancel')]"
    btn_confirm = "//button[contains(text(),'Confirm')]"
    advance_mode_confirm_text_field = "//body/reach-portal[9]/div[3]/div[1]/div[1]/div[1]/div[1]/input[1]"
