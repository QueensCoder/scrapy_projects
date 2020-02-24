function main(splash,args)


--set another user agent
 -- splash:set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9")

  
  --make custom headers to send with req
  --[[
  headers = {
    ['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
  }
  
  splash:set_custom_headers(headers)
  ]]
  
  --set user-agent using method that takes callback
  splash:on_request(function(request)
    request:set_header("User-Agent",'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9')
	end)

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