<script lang="ts">
  import TwitterPost from "./TwitterPost.svelte"

  let urls = $state(["https://twitter.com/elonmusk/status/1812258574049157405?ref_src=twsrc%5Etfw"]);
</script>
<main>
  <h2>Twitter</h2>
  <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
  {#each urls as url}
    <TwitterPost url={url} />
  {/each}
</main>





