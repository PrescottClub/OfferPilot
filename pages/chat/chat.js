let nextId = 1;

Page({
  data: {
    draft: '',
    quickPrompts: ['快速提问', '申请规划', '材料润色'],
    messages: [
      { id: nextId++, role: 'bot', text: '你好，我是OfferPilot，随时为你提供留学相关帮助～' }
    ],
    scrollIntoView: ''
  },
  onInput(e) {
    this.setData({ draft: e.detail.value });
  },
  onSend() {
    const text = (this.data.draft || '').trim();
    if (!text) return;
    this.dispatchMessage(text);
  },
  onQuickSelect(e) {
    const text = e.currentTarget.dataset.value;
    this.dispatchMessage(text);
  },
  dispatchMessage(text) {
    const userMsg = { id: nextId++, role: 'me', text };
    const userMessages = this.data.messages.concat(userMsg);
    this.setData({ messages: userMessages, draft: '', scrollIntoView: `msg-${userMsg.id}` });

    setTimeout(() => {
      const reply = { id: nextId++, role: 'bot', text: '收到：' + text };
      this.setData({
        messages: this.data.messages.concat(reply),
        scrollIntoView: `msg-${reply.id}`
      });
    }, 400);
  }
});
