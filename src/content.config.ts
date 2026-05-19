import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const useCases = defineCollection({
  loader: glob({
    pattern: '*/BRIEF.md',
    base: './',
  }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    type: z.enum(['new', 'existing']),
    origin: z.enum(['ongoing-project', 'funding-pipeline', 'data-gap']),
    status: z.enum([
      'idea',
      'brief',
      'active-development',
      'piloting',
      'handover',
      'complete',
      'on-hold',
      'no-go',
    ]),
    go_no_go: z
      .object({
        decision: z
          .enum(['pending', 'go', 'no-go', 'on-hold'])
          .default('pending'),
        date: z.string().nullable().optional(),
        decided_by: z.string().nullable().optional(),
        notes: z.string().nullable().optional(),
      })
      .optional(),
    champion: z.string(),
    coordinator: z.string().optional(),
    task_group: z.array(z.string()).default([]),
    primary_aow: z
      .enum([
        'AoW0-Orchestrate',
        'AoW1-Accelerate',
        'AoW2-Adapt',
        'AoW3-Empower',
        'AoW4-Transition',
        'AoW5-Finance',
      ])
      .optional(),
    related_aows: z.array(z.string()).default([]),
    ca_os_packages: z.array(z.string()).default([]),
    tags: z.array(z.string()).default([]),
    updated: z.coerce.date(),
  }),
});

export const collections = {
  'use-cases': useCases,
};
