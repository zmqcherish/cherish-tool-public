// document.body.bgColor = 'red';
var a = document.getElementsByClassName('el-input__inner');
a[0].value = '群媒体测试号'
// a[1].value = "公益"
a[1].click();
document.getElementsByClassName('el-select-dropdown__item')[1].click()
var b =  document.getElementsByClassName('el-textarea__inner')[0];
b.value = '群媒体测试号群媒体测试号群媒体测试号'

var evt = document.createEvent('HTMLEvents')
evt.initEvent('input', true, true)
a[0].dispatchEvent(evt)
b.dispatchEvent(evt)