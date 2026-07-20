# CarePulse — Odoo Practice Tasks for Clinics & Hospitals

*"Clinic operations, from patient to payment."*

A set of practice tasks for building a clinic/hospital management module in Odoo. Each task is written like a real client request, not a coding exercise. Build it, then record it if you're making a portfolio video.

## How to use this file

1. Start from Easy, move to Medium, then try Hard once you're comfortable.
2. Read the "Scenario" like it's an actual client sitting in front of you. That's the real skill — turning a vague request into a working system.
3. Some tasks say **Depends on** — do that task first, since the next one builds on it.
4. Tasks marked **Full Cycle** need 3-4 modules working together. These are the best ones to show in a video because they prove you understand how Odoo modules connect, not just isolated fixes.

## Difficulty guide

- 🟢 **Easy** — one module, basic configuration, good for warming up
- 🟡 **Medium** — one or two modules, some automation or logic, this is where most real work lives
- 🔴 **Hard** — three or more modules, real business logic, reporting across branches

---

### 🟢 M1. Patient Records
**Modules:** Contacts, CRM

**Scenario:** A small clinic currently keeps patient info on paper cards. The receptionist wants every patient searchable by name or phone, with allergies and blood type visible at a glance.

**What to build:** Add custom fields on the contact form for allergies, blood type, and emergency contact. Create tags to mark patient type (child, adult, elderly). Make a filtered list view showing only patients.

**Goal:** A receptionist can find any patient's medical basics in under 5 seconds.

**New skill:** Adding custom fields to an existing model and building saved filters.

---

### 🟢 M2. Appointment Reminders
**Modules:** Calendar, CRM

**Scenario:** Patients keep forgetting their appointments and the clinic loses money on no-shows.

**What to build:** Create appointment types (Checkup, Follow-up, Emergency) with different durations. Set up an automated email reminder sent 24 hours before the appointment.

**Goal:** No-show rate drops because every patient gets a reminder automatically, with zero manual work from staff.

**New skill:** Scheduled automated actions tied to a calendar event.

---

### 🟡 M3. Online Doctor Booking
**Modules:** Calendar, Website

**Scenario:** The clinic wants patients to book their own appointment online instead of calling in, but only during each doctor's actual working hours.

**What to build:** Set working hours per doctor, block out lunch breaks and days off, and connect this to an online booking page that only shows real available slots.

**Goal:** A patient books online and the slot they pick is guaranteed to be free — no double bookings, no calls needed.

**Depends on:** M2

---

### 🟡 M4. Lab Test Billing with Insurance Discount
**Modules:** Sales, Accounting

**Scenario:** Some patients pay full price for lab tests, others have insurance that covers 50% or 80%. The clinic needs this handled automatically, not with manual math every time.

**What to build:** Create lab test products with a base price. Build pricelists for each insurance provider that apply the right discount automatically when that customer is selected.

**Goal:** Front desk selects the patient, the correct discounted price shows up on the invoice with no manual calculation.

**New skill:** Pricelists based on customer group.

---

### 🟡 M5. Medicine Stock with Expiry Alerts
**Modules:** Inventory

**Scenario:** The pharmacy inside the hospital has lost money from medicine expiring unnoticed on the shelf, and sometimes runs out of common medicine without warning.

**What to build:** Track medicine using lot numbers with expiry dates. Set a minimum stock rule so the system automatically creates a purchase request when stock runs low. Set up a report showing medicine expiring within 30 days.

**Goal:** Pharmacist gets warned before medicine expires and before it runs out, instead of finding out too late.

**New skill:** Lot/expiry tracking and reordering rules.

---

### 🟡 M6. Nurse Shift Scheduling
**Modules:** Employees, Attendances

**Scenario:** The head nurse manually writes shift schedules on a whiteboard and it's a mess when someone calls in sick.

**What to build:** Set up working schedules for morning/night shifts per nurse. Use the attendance kiosk for check-in/check-out. Build a report showing who is on shift right now.

**Goal:** Head nurse can see, at any moment, exactly who is currently on duty.

---

### 🟡 M7. Patient Follow-up Pipeline
**Modules:** CRM

**Scenario:** After a diagnosis, patients need follow-up calls (test results, medicine check, recovery check), but the clinic keeps forgetting to call some of them.

**What to build:** Build a pipeline with stages: Consultation → Diagnosis → Treatment → Recovery Check. Add an automatic activity (a task reminder) that gets created for the doctor whenever a patient enters "Recovery Check."

**Goal:** No patient is forgotten — the system reminds the doctor to make the follow-up call.

**Depends on:** M1

---

### 🟡 M8. Full Cycle — Clinic Visit to Paid Invoice
**Modules:** CRM, Sales, Inventory, Accounting

**Scenario:** Right now a patient's visit, medicine, and payment are tracked in three different notebooks, and it's hard to know if a bill was actually paid.

**What to build:** Patient visit is logged as a CRM opportunity → consultation is quoted as a sale order → medicine dispensed is deducted from pharmacy stock automatically → invoice is generated from the sale order → payment is recorded and reconciled.

**Goal:** One patient visit, one continuous digital trail from arrival to paid invoice, with the pharmacy stock updating on its own.

**Depends on:** M1, M4, M5

---

### 🟡 M9. Insurance Company Debt Tracking
**Modules:** Accounting

**Scenario:** Insurance companies owe the hospital money for treatments already given, and finance has no clear view of how much each one owes or how overdue it is.

**What to build:** Set up each insurance company as a separate vendor/customer account. Track partial payments against invoices. Build an aging report showing how much is overdue and by how long.

**Goal:** Finance manager opens one report and instantly knows which insurance company owes what, and since when.

---

### 🔴 M10. Multi-Branch Hospital Dashboard
**Modules:** Accounting, Employees, Inventory

**Scenario:** A hospital group has 3 branches. Management wants one dashboard comparing revenue, doctor performance, and medicine stock across all branches — not three separate spreadsheets.

**What to build:** Set up each branch as a separate company/analytic account. Build a consolidated financial report by branch. Add a doctor performance KPI (patients seen, revenue generated). Add a stock reconciliation view comparing medicine levels across branches.

**Goal:** Management opens one screen and sees all 3 branches side by side — money, people, and stock.

---

## Best task for your portfolio video

**M8 — Full Cycle: Clinic Visit to Paid Invoice** is the strongest pick for CarePulse. It proves you can connect CRM, Sales, Inventory, and Accounting into one working flow — not just fix one isolated bug.
