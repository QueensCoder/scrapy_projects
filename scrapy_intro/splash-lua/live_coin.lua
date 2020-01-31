function main(splash, args)
    url = args.url
    assert(splash:go(url))
    assert(splash:wait(1))

    -- get coin tabs
    rur_tab = assert(splash:select_all(".filterPanelItem___2z5Gb"))
    -- click on 5th tab
    rur_tab[5]:mouse_click()
    assert(splash:wait(1))

    -- set viewport to full
    splash:set_viewport_full()
    return splash:png()
  end