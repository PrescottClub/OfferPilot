Page({
  data: {
    nickname: '',
    name: '',
    regions: [],
    regionsExpanded: false,
    allRegions: ['美国','加拿大','英国','法国','德国','澳大利亚','新西兰'],
    score: '',
    schools: '',
    majors: ''
  },
  onName(e) {
    this.setData({ name: e.detail.value });
  },
  onRegions(e) {
    this.setData({ regions: e.detail.value });
  },
  onScore(e) {
    this.setData({ score: e.detail.value });
  },
  onSchools(e) {
    this.setData({ schools: e.detail.value });
  },
  onMajors(e) {
    this.setData({ majors: e.detail.value });
  },
  toggleRegions() {
    this.setData({ regionsExpanded: !this.data.regionsExpanded });
  },
  onSave() {
    wx.showToast({ title: '已保存', icon: 'success' });
  }
});
