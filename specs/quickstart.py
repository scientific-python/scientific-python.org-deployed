"""
SPEC Quickstart
===============

Quickly setup stub for new SPEC proposal.
"""

from datetime import datetime

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".tools"))
from tools import prompt


now = datetime.now()
author = prompt("Your Name")
email = prompt("Your Email Address")
number = prompt("SPEC number", validate=lambda x: int(x))
title = prompt("SPEC title")

filename = f"spec-{number:04d}/index.md"
text = f"""---
title: "SPEC {number} — {title}"
date: {now.strftime("%Y-%m-%d")}
author:
  - "{author} <{email}>"
discussion: https://discuss.scientific-python.org/t/
endorsed-by:
---

## Description

<!--
Briefly and clearly describe the proposal.
Explain the general need and the advantages of this specific proposal.
If relevant, include examples of how the new functionality would be used,
intended use-cases, and pseudo-code illustrating its use.
-->

## Implementation

<!--
Discuss how this would be implemented.
-->

### Core Project Endorsement

<!--
Discuss what it means for a core project to endorse this SPEC.
-->

### Ecosystem Adoption

<!--
Discuss what it means for a project to adopt this SPEC.
-->

## Notes

<!--
Include a bulleted list of annotated links, comments,
and other ancillary information as needed.
-->
"""

os.makedirs(os.path.dirname(filename), exist_ok=True)
with open(filename, "w") as file:
    file.write(text)
