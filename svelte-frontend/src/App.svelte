<script lang="ts">
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Instagram from './lib/Instagram.svelte'
  import Twitter from './lib/Twitter.svelte'
  // import Facebook from './lib/Facebook.svelte'
  import TikTok from "./lib/TikTok.svelte"
</script>
<main>
  <h1>Multi Feed</h1>

  <div class="grid">
    <div class="item">
      <Instagram />
    </div>

    <div class="item">
      <Twitter />
    </div>

    <div class="item">
      <TikTok />
    </div>
  </div>
</main>

<style>
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr); /* 3 equal columns */
    gap: 10px; /* Spacing between items */
  }

  .item {
    text-align: center;
    border-radius: 8px;
  }
</style>
