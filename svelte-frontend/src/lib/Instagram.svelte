<script lang="ts">
  import InstagramPost from "./InstagramPost.svelte"

  let rawUrls = $state(["/reel/DDh3JfYoD56"]);
  let fullUrls = $derived(rawUrls.map(url => `https://www.instagram.com${url}/?utm_source=ig_embed&amp;utm_campaign=loading`));

  $inspect(fullUrls);
</script>
<main>
<script async src="//www.instagram.com/embed.js"></script>
<h2>Instagram</h2>
  {#each fullUrls as url}
    <InstagramPost url={url} />
  {/each}
</main>

