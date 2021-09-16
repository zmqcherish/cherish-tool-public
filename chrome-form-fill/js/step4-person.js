// document.body.bgColor = 'red';
var evt = document.createEvent('HTMLEvents')
evt.initEvent('input', true, true)
var a = document.getElementsByClassName('el-input__inner');
a[0].value = '张广红'
a[0].dispatchEvent(evt)

// a[1].value = '北京市'
// a[2].value = '东城区'
a[1].click();
document.getElementsByClassName('el-select-dropdown__item')[1].click()

a[3].value = '地址地址地址'
a[3].dispatchEvent(evt)
a[4].value = 'hebe@tien.com'
a[4].dispatchEvent(evt)
a[6].value = '18614093620'
a[6].dispatchEvent(evt)

var c = document.getElementsByClassName('el-checkbox__inner');
c[0].click()