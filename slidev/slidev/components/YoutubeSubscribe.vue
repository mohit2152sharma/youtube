<template>
  <button class="yt-subscribe">
    <span class="yt-icon">
      <svg viewBox="0 0 24 24" width="28" height="28" fill="currentColor" aria-hidden="true">
        <g>
          <path d="M23.498 6.186a2.997 2.997 0 0 0-2.112-2.12C19.228 3.5 12 3.5 12 3.5s-7.228 0-9.386.566A2.997 2.997 0 0 0 .502 6.186C0 8.35 0 12 0 12s0 3.65.502 5.814a2.997 2.997 0 0 0 2.112 2.12C4.772 20.5 12 20.5 12 20.5s7.228 0 9.386-.566a2.997 2.997 0 0 0 2.112-2.12C24 15.65 24 12 24 12s0-3.65-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"/>
        </g>
      </svg>
    </span>
    <span class="yt-text">Subscribe</span>
  </button>
</template>

<script setup lang="ts">
// No props needed
</script>

<style scoped>
.yt-subscribe {
  display: flex;
  align-items: center;
  gap: 0.5em;
  background: #ff0000;
  color: #fff;
  border: none;
  border-radius: 999px;
  padding: 0.5em 1.2em 0.5em 0.8em;
  font-weight: 700;
  font-size: 1.1em;
  cursor: pointer;
  box-shadow: 0 2px 8px 0 #0002;
  transition: background 0.15s;
}
.yt-subscribe:hover {
  background: #e60000;
}
.yt-icon {
  display: flex;
  align-items: center;
}
.yt-text {
  letter-spacing: 0.03em;
  text-shadow: 0 1px 2px #0003;
}
</style> 