function main(splash,args)
  url = args.url

  --   assert makes sure the operation goes through and splash can go to the url
  assert(splash:go(url))

  --   wait is recommened with JS heavy websites so the site can load properly 
  assert(splash:wait(1))
  
  input_box = assert(splash:select("#search_form_input_homepage"))
  input_box:focus()
  input_box:send_text("my user agent")
  assert(splash:wait(1))
  
  --can select button and click 
  --[[
  btn = assert(splash:select("#search_button_homepage"))
  btn:mouse_click()
  ]]
  
  --or just send enter key to perform search
  input_box:send_keys("<Enter>")
  assert(splash:wait(3))

  --make viewport full to see
  splash:set_viewport_full()
  
  -- renders duckgogo html and png
  return {
    image = splash:png(),
    html = splash:html()
  }
end