var evt = document.createEvent('HTMLEvents')
evt.initEvent('input', true, true)

var a = document.getElementsByClassName('el-input__inner');

// a[1].value = '北京市'
// a[2].value = '东城区'

a[1].click();
document.getElementsByClassName('el-select-dropdown__item')[1].click()

a[0].value = '机构名称机构名称机构名称'
a[3].value = '地址地址地址'
a[4].value = '123456'
a[6].value = '张广红'
a[7].value = 'hebe@tien.com'
a[8].value = '18614093620'

a[0].dispatchEvent(evt)
a[3].dispatchEvent(evt)
a[4].dispatchEvent(evt)
a[6].dispatchEvent(evt)
a[7].dispatchEvent(evt)
a[8].dispatchEvent(evt)

var c = document.getElementsByClassName('el-checkbox__inner');
c[0].click()