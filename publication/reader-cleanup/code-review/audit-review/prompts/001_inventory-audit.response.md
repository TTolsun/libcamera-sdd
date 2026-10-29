{
  "findings": [
    "The proposed changes are generally value-preserving only if the stated exact-match conditions are checked against the rendered controls and full generated data. The inventory does not provide footer URLs, answer-link targets, or every central-index row, so it cannot establish that those conditions are met.",
    "component-index.html repeats its introductory paragraph verbatim, and scenarios/index.html does the same. Each can retain one copy without losing supplied information.",
    "The eight-row camera-stack evidence table is identical in index.html, team-overview.html, and vendor-overview.html. These pages serve different entry points, so consolidation should preserve access to the diagram’s evidence from each context.",
    "The complete related-class tables in camera-model.html and camera-requests.html are identical; so are those in ipa.html and ipa-algorithms.html, and those in ipu3-lsc-flow.html and ipu3-lsc-prepare.html. The latter seven rows also appear in the eight-row table in ipu3-lsc.html, which adds IPASessionConfiguration. The supplied index samples do not establish a unique full-row match for every row.",
    "The request-ownership evidence tables in camera-requests.html and request-lifecycle.html share a heading, count, and samples; the waiting-request tables in pipeline-requests.html and request-diagnosis.html do too. Their unsampled rows are unavailable, so full duplication is not verified.",
    "In camera_stop, queue_request, and complete_request, a boundary entry repeats a checkpoint’s target, boundary note, and citation. In camera_start, the two boundary rows provide separate citations that the checkpoint combines. A consolidation must retain each citation and the distinction between a checkpoint and its boundary.",
    "The design-question tables carry meaningful scope qualifiers, including separate execution checks and the connection-disconnect limit in camera-model.html. Scenario boundary notes likewise distinguish unresolved dynamic dispatch from method-transfer targets; these distinctions must survive conversion.",
    "The component index and folded scenario traces contain substantial reference data, but size or repeated wording alone does not establish that their rows are redundant. The inventory supplies samples rather than all rows for many tables."
  ],
  "recommendations": [
    "Remove the two confirmed duplicate introductory paragraphs, retaining one copy on each page.",
    "Apply footer deduplication only after comparing both the actual URL and visible label. Preserve both controls when either differs or cannot be verified.",
    "Group homepage status entries by their exact check and approval labels, keeping every page link and every non-passing or unapproved state visible.",
    "Convert the generated design-question tables to lists only when every question, answer link, and distinct scope qualifier is preserved. Retain custom tables and markup.",
    "Replace related-class tables with direct index-row links only after verifying every complete row against a unique matching index row. Otherwise retain the table or the unmatched rows.",
    "Consider a shared evidence target for the confirmed camera-stack table, with direct access from all three pages. Verify the complete rows and reader context before consolidating the two partially sampled table pairs.",
    "For single-row scenario tables, use labeled definition lists with citations and boundary notes intact. Where a checkpoint and boundary entry are confirmed duplicates, combine their presentation only if both roles remain clear.",
    "Preserve all other tables, facts, manuscript bytes, inspectors, diagrams, source hashes, old IDs, approval states, and custom markup as planned. Automatic review does not constitute human approval."
  ]
}
