# Neural_Coreferencing

# How it works!!!
Neural coreference resolution models usually involve various components, such as:
<ol>
  <li><b>Feature Extraction:</b> Detecting the different parts of a sentence and their relationships with each other.</li>
  <li><b>Mention Detection:</b> Identifying potential words or phrases (mentions) that may be involved in coreference relations (they all refer to the same entity).</li>
  <li><b>Pairwise Scoring:</b> Computing a score for each pair of mentions, representing the likelihood that they corefer.</li>
  <li><b>Clustering:</b> Grouping mentions into clusters, where each cluster represents a single entity or concept.</li>
  <li><b>Replacement:</b> For the last message in the conversation (or for all messages succeeding the first), replace the phrases in each cluster by the common word that gives the entire picture.</li>
