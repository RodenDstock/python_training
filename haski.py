{
  "id": "7df66f5e-af74-4afe-b7b7-d84e2af5eeb2",
  "version": "2.0",
  "name": "haski",
  "url": "https://xn--80ahnhilx4a.xn--p1ai",
  "tests": [{
    "id": "8ffd06aa-de94-4d01-afa9-bfa206fe3e1c",
    "name": "Haski",
    "commands": [{
      "id": "325e21e0-0ae5-4a9b-9024-5b0fb156c669",
      "comment": "",
      "command": "open",
      "target": "/",
      "targets": [],
      "value": ""
    }, {
      "id": "f7982898-3ea6-456e-8d25-0f5c89907502",
      "comment": "",
      "command": "setWindowSize",
      "target": "1936x1096",
      "targets": [],
      "value": ""
    }, {
      "id": "38154262-cff0-4fd7-8fe6-3c78802c9bb1",
      "comment": "",
      "command": "mouseOver",
      "target": "css=#menu-item-296 .text-wrap",
      "targets": [
        ["css=#menu-item-296 .text-wrap", "css:finder"],
        ["xpath=//li[@id='menu-item-296']/a/span", "xpath:idRelative"],
        ["xpath=//nav/ul/li/a/span", "xpath:position"],
        ["xpath=//span[contains(.,'Главная')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "cf65d9e3-d024-4971-96ea-0877ce9cd04b",
      "comment": "",
      "command": "mouseOut",
      "target": "css=#menu-item-296 .text-wrap",
      "targets": [
        ["css=#menu-item-296 .text-wrap", "css:finder"],
        ["xpath=//li[@id='menu-item-296']/a/span", "xpath:idRelative"],
        ["xpath=//nav/ul/li/a/span", "xpath:position"],
        ["xpath=//span[contains(.,'Главная')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "87eba7bf-e60b-41db-9782-19650e1e2a2e",
      "comment": "",
      "command": "click",
      "target": "linkText=Главная",
      "targets": [
        ["linkText=Главная", "linkText"],
        ["css=#menu-item-296 > .menu-link", "css:finder"],
        ["xpath=//li[@id='menu-item-296']/a", "xpath:idRelative"],
        ["xpath=(//a[contains(@href, 'https://xn--80ahnhilx4a.xn--p1ai/')])[2]", "xpath:href"],
        ["xpath=//nav/ul/li/a", "xpath:position"],
        ["xpath=//a[contains(.,'Главная')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "7671916a-c356-4e07-bcf0-9d69d63415e1",
      "comment": "",
      "command": "click",
      "target": "css=#menu-item-308 .text-wrap",
      "targets": [
        ["css=#menu-item-308 .text-wrap", "css:finder"],
        ["xpath=//li[@id='menu-item-308']/a/span", "xpath:idRelative"],
        ["xpath=//nav/ul/li[2]/a/span", "xpath:position"],
        ["xpath=//span[contains(.,'Новости и статьи')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "6c250c2a-f472-478b-a6b7-b9f91b3247a9",
      "comment": "",
      "command": "click",
      "target": "css=#menu-item-666 > .menu-link > .text-wrap",
      "targets": [
        ["css=#menu-item-666 > .menu-link > .text-wrap", "css:finder"],
        ["xpath=//li[@id='menu-item-666']/a/span", "xpath:idRelative"],
        ["xpath=//nav/ul/li[3]/a/span", "xpath:position"],
        ["xpath=//span[contains(.,'Щенки. Собаки на пристройство ')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "fa4adcc4-a3b9-41a6-b073-8585b4837f53",
      "comment": "",
      "command": "click",
      "target": "css=#menu-item-371 .text-wrap",
      "targets": [
        ["css=#menu-item-371 .text-wrap", "css:finder"],
        ["xpath=//li[@id='menu-item-371']/a/span", "xpath:idRelative"],
        ["xpath=//li[4]/ul/li/a/span", "xpath:position"],
        ["xpath=//span[contains(.,'Посещение Дома Хаски Сергиев Посад')]", "xpath:innerText"]
      ],
      "value": ""
    }, {
      "id": "b77cd5f8-6c75-4e0f-a11c-9c52f127279f",
      "comment": "",
      "command": "runScript",
      "target": "window.scrollTo(0,205)",
      "targets": [],
      "value": ""
    }, {
      "id": "86f1cfc0-f05e-4733-b235-60f671cef654",
      "comment": "",
      "command": "click",
      "target": "css=#search-2 #s",
      "targets": [
        ["css=#search-2 #s", "css:finder"],
        ["xpath=(//input[@id='s'])[2]", "xpath:attributes"],
        ["xpath=(//form[@id='searchform']/input)[2]", "xpath:idRelative"],
        ["xpath=//div[2]/form/input", "xpath:position"]
      ],
      "value": ""
    }, {
      "id": "68ff08fe-6c77-40a5-ac65-829a4cc596d2",
      "comment": "",
      "command": "type",
      "target": "css=#search-2 #s",
      "targets": [
        ["css=#search-2 #s", "css:finder"],
        ["xpath=(//input[@id='s'])[2]", "xpath:attributes"],
        ["xpath=(//form[@id='searchform']/input)[2]", "xpath:idRelative"],
        ["xpath=//div[2]/form/input", "xpath:position"]
      ],
      "value": "Ноябрь"
    }, {
      "id": "e8febd80-e14b-4b8e-8a15-cde2c89aa2ce",
      "comment": "",
      "command": "sendKeys",
      "target": "css=#search-2 #s",
      "targets": [
        ["css=#search-2 #s", "css:finder"],
        ["xpath=(//input[@id='s'])[2]", "xpath:attributes"],
        ["xpath=(//form[@id='searchform']/input)[2]", "xpath:idRelative"],
        ["xpath=//div[2]/form/input", "xpath:position"]
      ],
      "value": "${KEY_ENTER}"
    }]
  }],
  "suites": [{
    "id": "298547b6-52a3-4073-a33d-4db4879af912",
    "name": "Default Suite",
    "persistSession": false,
    "parallel": false,
    "timeout": 300,
    "tests": ["8ffd06aa-de94-4d01-afa9-bfa206fe3e1c"]
  }],
  "urls": ["https://xn--80ahnhilx4a.xn--p1ai/"],
  "plugins": []
}