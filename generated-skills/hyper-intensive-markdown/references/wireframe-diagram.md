# Wireframe Diagram Patterns

Prefer Mermaid flowcharts for quick, sketch-style wireframes. Keep diagrams small and readable.

## Pattern 1: Simple Page Layout

```mermaid
flowchart TB
  subgraph Page[<Page Name>]
    Header[Header]
    Nav[Navigation]
    Content[Main Content]
    Footer[Footer]
  end
  Header --> Content
  Nav --> Content
```

## Pattern 2: Component Boundary Map

```mermaid
flowchart LR
  subgraph Container[<Container Component>]
    A[<Child A>]
    B[<Child B>]
    C[<Child C>]
  end
  A --> B
  B --> C
```

## ASCII Fallback (when Mermaid is not allowed)

```
+------------------------+
| Header                 |
+-----------+------------+
| Nav       | Content    |
|           |            |
+-----------+------------+
| Footer                 |
+------------------------+
```
