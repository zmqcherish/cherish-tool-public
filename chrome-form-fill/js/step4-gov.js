var evt = document.createEvent('HTMLEvents')
evt.initEvent('input', true, true)

var a = document.getElementsByClassName('el-input__inner');

// a[1].value = '国家级'
// a[4].value = '北京市'
// a[5].value = '东城区'
a[1].click();
document.getElementsByClassName('el-select-dropdown__item')[1].click()
a[4].click()
document.getElementsByClassName('el-select-dropdown__item')[15].click()

a[0].value = '单位名称单位名称单位名称'
a[2].value = '010-11111111'
a[3].value = 'hebe@tien.com'
a[6].value = '地址地址地址'
a[7].value = '123456'
a[8].value = '张广红'
a[9].value = 'hebe2@tien.com'
a[10].value = '18614093620'

a[0].dispatchEvent(evt)
a[2].dispatchEvent(evt)
a[3].dispatchEvent(evt)
a[6].dispatchEvent(evt)
a[7].dispatchEvent(evt)
a[8].dispatchEvent(evt)
a[9].dispatchEvent(evt)
a[10].dispatchEvent(evt)

var c = document.getElementsByClassName('el-checkbox__inner');
c[0].click()