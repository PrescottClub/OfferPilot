const PROFILE_STORAGE_KEY = 'offerPilot.profile.v1';
const PROFILE_FIELDS = ['nickname', 'name', 'regions', 'score', 'schools', 'majors'];
const AUTO_SAVE_HINT_DURATION = 1600;
const SKELETON_DELAY = 420;

function extractProfileFields(source) {
  const target = {};
  PROFILE_FIELDS.forEach(key => {
    if (Object.prototype.hasOwnProperty.call(source, key)) {
      target[key] = source[key];
    }
  });
  return target;
}

function loadProfileFromStorage() {
  try {
    const stored = wx.getStorageSync(PROFILE_STORAGE_KEY);
    if (!stored || typeof stored !== 'object') {
      return null;
    }
    return extractProfileFields(stored);
  } catch (err) {
    console.warn('Failed to load profile from storage', err);
    return null;
  }
}

function persistProfileSnapshot(data) {
  const payload = extractProfileFields(data);
  try {
    wx.setStorageSync(PROFILE_STORAGE_KEY, payload);
    return true;
  } catch (err) {
    console.warn('Failed to save profile to storage', err);
    return false;
  }
}

Page({
  data: {
    isReady: true,
    isLoading: true,
    nickname: '',
    name: '',
    regions: [],
    regionsExpanded: false,
    allRegions: ['美国', '加拿大', '英国', '法国', '德国', '澳大利亚', '新西兰'],
    regionFlags: {
      '美国': 'flag-us',
      '加拿大': 'flag-ca',
      '英国': 'flag-uk',
      '法国': 'flag-fr',
      '德国': 'flag-de',
      '澳大利亚': 'flag-au',
      '新西兰': 'flag-nz'
    },
    score: '',
    schools: '',
    majors: '',
    saveState: 'idle',
    saveHint: '',
    skeletonRows: [0, 1, 2, 3, 4]
  },
  onLoad() {
    const stored = loadProfileFromStorage();
    if (stored) {
      this.setData(stored);
    }
    this.startSkeleton();
  },
  onReady() {},
  onHide() {
    this.teardown();
  },
  onUnload() {
    this.teardown();
  },
  onName(e) {
    this.updateProfileField('name', e.detail.value || '');
  },
  onRegions(e) {
    this.updateProfileField('regions', e.detail.value || []);
  },
  onScore(e) {
    this.updateProfileField('score', e.detail.value || '');
  },
  onSchools(e) {
    this.updateProfileField('schools', e.detail.value || '');
  },
  onMajors(e) {
    this.updateProfileField('majors', e.detail.value || '');
  },
  toggleRegions() {
    this.setData({ regionsExpanded: !this.data.regionsExpanded });
  },
  onSave() {
    this.setData({ saveState: 'saving' });
    const ok = this.persistProfile();
    if (ok) {
      this.showSaveHint('资料已更新', 'saved', 2000);
      wx.showToast({ title: '已保存', icon: 'success' });
    } else {
      this.setData({ saveState: 'idle' });
      wx.showToast({ title: '保存失败', icon: 'none' });
    }
  },
  updateProfileField(key, value) {
    this.setData({ [key]: value }, () => {
      const ok = this.persistProfile();
      if (ok) {
        this.showSaveHint('已自动保存', 'synced');
      }
    });
  },
  showSaveHint(message, state = 'synced', duration = AUTO_SAVE_HINT_DURATION) {
    if (this.saveHintTimer) {
      clearTimeout(this.saveHintTimer);
      this.saveHintTimer = null;
    }
    this.setData({ saveHint: message, saveState: state });
    this.saveHintTimer = setTimeout(() => {
      this.setData({ saveHint: '', saveState: 'idle' });
      this.saveHintTimer = null;
    }, duration);
  },
  startSkeleton() {
    this.clearLoadingTimer();
    this.setData({ isLoading: true });
    this.loadingTimer = setTimeout(() => {
      this.setData({ isLoading: false });
      this.loadingTimer = null;
    }, SKELETON_DELAY);
  },
  persistProfile() {
    return persistProfileSnapshot(this.data);
  },
  clearLoadingTimer() {
    if (this.loadingTimer) {
      clearTimeout(this.loadingTimer);
      this.loadingTimer = null;
    }
  },
  teardown() {
    this.clearLoadingTimer();
    if (this.saveHintTimer) {
      clearTimeout(this.saveHintTimer);
      this.saveHintTimer = null;
    }
  }
});
