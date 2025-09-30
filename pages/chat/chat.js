let nextId = 1;

Page({
  data: {
    draft: '',
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

    const userMsg = { id: nextId++, role: 'me', text };
    const msgs = this.data.messages.concat(userMsg);
    this.setData({ messages: msgs, draft: '', scrollIntoView: `msg-${userMsg.id}` });

    // Mock bot reply
    setTimeout(() => {
      const reply = { id: nextId++, role: 'bot', text: '收到：' + text };
      this.setData({
        messages: this.data.messages.concat(reply),
        scrollIntoView: `msg-${reply.id}`
      });
    }, 400);
  }
})

