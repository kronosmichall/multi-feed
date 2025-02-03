<script>
  import TikTokPost from "./TikTokPost.svelte"
  let urls = $state([]);

</script>
<main>
<script async src="https://www.tiktok.com/embed.js"></script>
  {#each urls as url}
    <TikTokPost url={url} />
  {/each}
</main>
