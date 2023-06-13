# Neural_Coreferencing
Neural coreference resolution (overview) is a natural language processing (NLP) task that involves identifying when two or more words or phrases in a text refer to the same entity or concept. This process is crucial for understanding the context and meaning of a text, as it helps in resolving ambiguities and connecting different parts of a text.

# How it works!!!
Neural coreference resolution models usually involve various components, such as:
<ol>
  <li><b>Feature Extraction:</b> Detecting the different parts of a sentence and their relationships with each other.</li>
  <li><b>Mention Detection:</b> Identifying potential words or phrases (mentions) that may be involved in coreference relations (they all refer to the same entity).</li>
  <li><b>Pairwise Scoring:</b> Computing a score for each pair of mentions, representing the likelihood that they corefer.</li>
  <li><b>Clustering:</b> Grouping mentions into clusters, where each cluster represents a single entity or concept.</li>
  <li><b>Replacement:</b> For the last message in the conversation (or for all messages succeeding the first), replace the phrases in each cluster by the common word that gives the entire picture.</li>
  <li><b>Deployment:</b> Deploy the above setup as a part of ai-tools package such that it can be dockerized and then accessed through an API setup.</li>
</ol>
