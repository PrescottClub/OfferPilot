Page({
  data: {
    search: '',
    tools: [
      { name: '雅思口语练习', emoji: '🗣️' },
      { name: '文书批改', emoji: '📝' },
      { name: '留学问答社区', emoji: '👥' },
      { name: '签证办理指南', emoji: '🛂' },
      { name: '面试题库', emoji: '💼' },
      { name: '院校数据库', emoji: '🎓' }
    ],
    filteredTools: []
  },
  onLoad() {
    this.setData({ filteredTools: this.data.tools });
  },
  onSearchInput(e) {
    this.setData({ search: e.detail.value });
  },
  onSearch() {
    const q = (this.data.search || '').trim();
    const filtered = !q
      ? this.data.tools
      : this.data.tools.filter(t => t.name.includes(q));
    this.setData({ filteredTools: filtered });
  },
  onToolTap(e) {
    const name = e.currentTarget.dataset.name;
    wx.showToast({ title: name, icon: 'none' });
  }
})

