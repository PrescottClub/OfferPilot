let nextId = 1;
const BOT_REPLY_DELAY = 700;

Page({
  data: {
    isReady: false,
    draft: '',
    canSend: false,
    sending: false,
    sendPulse: false,
    quickPrompts: ['快速提问', '申请规划', '材料润色'],
    messages: [
      { id: nextId++, role: 'bot', text: '你好，我是OfferPilot，随时为你提供留学相关帮助～' }
    ],
    scrollIntoView: ''
  },
  onReady() {
    wx.nextTick(() => {
      setTimeout(() => {
        this.setData({ isReady: true });
      }, 30);
    });
  },
  onHide() {
    this.clearTypingPreview();
    this.clearSendPulseTimer();
  },
  onUnload() {
    this.clearTypingPreview();
    this.clearSendPulseTimer();
  },
  onInput(e) {
    const draft = e.detail.value || '';
    this.setData({ draft, canSend: draft.trim().length > 0 });
  },
  onSend() {
    if (!this.data.canSend || this.data.sending) return;
    const text = (this.data.draft || '').trim();
    if (!text) return;
    this.dispatchMessage(text);
  },
  onQuickSelect(e) {
    const text = e.currentTarget.dataset.value;
    if (!text) return;
    this.dispatchMessage(text);
  },
  dispatchMessage(text) {
    const baseMessages = this.clearTypingPreview({ silent: true });
    const userMsg = { id: nextId++, role: 'me', text };
    const typingMsg = { id: nextId++, role: 'bot', typing: true };
    const updatedMessages = baseMessages.concat(userMsg, typingMsg);

    this.setData({
      messages: updatedMessages,
      draft: '',
      canSend: false,
      scrollIntoView: `msg-${typingMsg.id}`,
      sending: true
    });

    this.triggerSendPulse();
    this.triggerHaptic();

    this.typingTimer = setTimeout(() => {
      const reply = { id: nextId++, role: 'bot', text: '收到：' + text };
      const withoutTyping = this.data.messages.filter(msg => msg.id !== typingMsg.id);
      this.setData({
        messages: withoutTyping.concat(reply),
        scrollIntoView: `msg-${reply.id}`,
        sending: false
      });
      this.typingTimer = null;
    }, BOT_REPLY_DELAY);
  },
  clearTypingPreview(options = {}) {
    if (this.typingTimer) {
      clearTimeout(this.typingTimer);
      this.typingTimer = null;
    }
    const cleaned = this.data.messages.filter(msg => !msg.typing);
    if (!options.silent && cleaned.length !== this.data.messages.length) {
      this.setData({ messages: cleaned });
    }
    return cleaned;
  },
  clearSendPulseTimer() {
    if (this.sendPulseTimer) {
      clearTimeout(this.sendPulseTimer);
      this.sendPulseTimer = null;
    }
    if (this.data.sendPulse) {
      this.setData({ sendPulse: false });
    }
  },
  triggerSendPulse() {
    this.clearSendPulseTimer();
    this.setData({ sendPulse: true });
    this.sendPulseTimer = setTimeout(() => {
      this.setData({ sendPulse: false });
      this.sendPulseTimer = null;
    }, 240);
  },
  triggerHaptic() {
    if (wx.vibrateShort) {
      wx.vibrateShort({ type: 'light' });
    }
  }
});
