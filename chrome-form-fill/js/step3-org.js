var evt = document.createEvent('HTMLEvents')
evt.initEvent('input', true, true)

var a = document.getElementsByClassName('el-input__inner');
a[0].value = '企业测试号'
// a[1].value = "公益"
a[1].click();
document.getElementsByClassName('el-select-dropdown__item')[1].click()
var b =  document.getElementsByClassName('el-textarea__inner')[0];
b.value = '企业测试号企业测试号企业测试号'

a[0].dispatchEvent(evt)
b.dispatchEvent(evt)