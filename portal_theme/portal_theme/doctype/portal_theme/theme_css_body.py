css_body = """
		/* ------------------------------------------------------- */
		/*  PART 1 — ROOT VARIABLES                                */
		/* ------------------------------------------------------- */
		:root {
			--ws-bg: var(--primary-100);
			--ws-card-bg: var(--primary-100);
			--ws-border: var(--accent-100);
			--ws-primary: var(--primary-200);
			--ws-accent: var(--primary-100);
			--ws-accent-light: var(--accent-200);
			--ws-accent-soft: var(--primary-100);
			--ws-accent-dark: var(--primary-300);
			--ws-radius: 6px;
			--ws-radius-standard: 12px;
			--ws-shadow: 0 4px 14px rgba(0,0,0,0.06);
			--icon-stroke: var(--secondary-300);
		}

        


        
		/* ------------------------------------------------------- */
		/*  PART 2 — GENERIC COMMON ELEMENT STYLES                 */
		/* ------------------------------------------------------- */

		/* Buttons */
		.btn-new-workspace,
		.btn-edit-workspace {
			background-color: var(--ws-accent-soft) !important;
			color: var(--ws-accent-dark) !important;
			font-weight: 600 !important;
			border-radius: var(--ws-radius) !important;
			padding: 6px 14px !important;
			box-shadow: var(--ws-shadow) !important;
			transition: 0.2s ease all;
		}

		.btn-new-workspace:hover,
		.btn-edit-workspace:hover {
			transform: translateY(-3px);
			box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
		}

		/* Inputs / Controls */
		.control-input:not(:has(button)) {
			border-radius: var(--ws-radius);
			border: 1px solid #ccc;
			transition: 0.2s;
		}

		.form-in-grid {
			border-radius: var(--ws-radius);
			border: 1px solid #ccc;
		}

		/* Standard Filter Section */
		.standard-filter-section .form-control,
		.standard-filter-section input[type="text"] {
			background: #fff !important;
			border: 1px solid #000 !important;
			color: #222 !important;
			border-radius: 7px !important;
			padding: 6px 12px !important;
			transition: 0.2s;
		}

		.standard-filter-section .form-control:focus {
			border-color: var(--ws-accent) !important;
			box-shadow: 0 0 0 2px var(--ws-card-bg);
		}

		.standard-filter-section .form-group {
			margin-bottom: 12px;
		}

		/* List Row Styling */
		.list-row-container {
			border-top: 1px #c4c4c4 solid !important;
		}

		.list-row-container:nth-of-type(even) {
			background-color: #f5f5f5 !important;
			border-top: 1px #c4c4c4 solid !important;
		}

		/* Datatable Rows */
		.datatable .dt-row:not(.dt-row-header):nth-of-type(odd) .dt-cell {
			background-color: #f1f1f1 !important;
		}





		/* ------------------------------------------------------- */
		/*  PART 3 — PAGE / COMPONENT SPECIFIC STYLES              */
		/* ------------------------------------------------------- */

		/* ---------------- NAVBAR ---------------- */
		.navbar {
			background: linear-gradient(
				90deg,
				var(--ws-accent),
				var(--ws-accent-light)
			) !important;
		}

		.navbar .awesomplete .form-control {
			border: 1px solid var(--ws-border) !important;
			border-radius: 6px;
		}

		.navbar .awesomplete .form-control:hover {
			box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
		}

		.nav.navbar-nav a {
			color: #000 !important;
			font-weight: 600 !important;
		}



		/* ---------------- WORKSPACE BODY & TITLE ---------------- */
		.workspace-body {
			background: var(--ws-primary) !important;
			padding-top: 10px;
		}

		.workspace-title .title-text {
			font-size: 26px !important;
			font-weight: 600 !important;
			color: #333 !important;
		}



		/* ---------------- SIDEBAR ---------------- */
		.workspace-sidebar {
			background: #fff !important;
			border-radius: var(--ws-radius) !important;
			border-right: 1px solid #eee !important;
		}

		.workspace-sidebar .sidebar-item {
			border-radius: var(--ws-radius) !important;
			padding: 10px 14px !important;
			margin-bottom: 6px !important;
			transition: 0.2s ease all;
			font-weight: 600 !important;
		}

		.workspace-sidebar .sidebar-item:hover {
			background: rgba(125, 42, 232, 0.06) !important;
		}

		.workspace-sidebar .sidebar-item.selected {
			background: var(--ws-primary) !important;
			color: #fff !important;
		}



		/* ---------------- WIDGET GRID & CARDS ---------------- */
		.widget-group {
			display: grid !important;
			grid-template-columns: repeat(auto-fill, minmax(260px, 1fr)) !important;
			gap: 18px !important;
		}

		.widget {
			background: var(--ws-card-bg) !important;
			border: 1px solid var(--ws-border) !important;
			border-radius: var(--ws-radius) !important;
			padding: 18px !important;
			box-shadow: var(--ws-shadow) !important;
			transition: 0.25s ease all;
		}

		.widget:hover {
			transform: translateY(-3px);
			box-shadow: 0 6px 20px rgba(0,0,0,0.1) !important;
		}

		.widget.spacer {
			display: none !important;
		}

		/* Widget Titles */
		.widget .widget-head,
		.widget .widget-title .ellipsis {
			font-size: 16px !important;
			font-weight: 600 !important;
			color: var(--ws-primary) !important;
		}



		/* ---------------- WIDGET LINKS ---------------- */
		.widget-body a {
			color: #555 !important;
		}

		.widget-body a:hover {
			color: var(--ws-primary) !important;
		}

		.widget-body .link-item {
			position: relative;
			padding-left: 20px !important;
			display: flex;
			align-items: center;
			margin-bottom: 6px;
		}

		.widget-body .link-item::before {
			content: "•";
			position: absolute;
			left: 0;
			top: 4px;
			font-size: 18px;
			color: var(--ws-primary);
		}

		.widget-body .link-item:hover::before {
			color: var(--ws-card-bg);
		}



		/* ---------------- SHORTCUT WIDGET ---------------- */
		.shortcut-widget-box {
			background: var(--ws-card-bg) !important;
			border-radius: var(--ws-radius) !important;
			padding: 14px !important;
			font-size: 15px !important;
			box-shadow: var(--ws-shadow) !important;
		}

		.shortcut-widget-box:hover {
			background: rgba(125, 42, 232, 0.05) !important;
		}



		/* ---------------- EDITOR HEADER ---------------- */
		.ce-header .h4 {
			color: var(--ws-primary) !important;
		}



		/* ---------------- HIDE EXTRA ELEMENTS ---------------- */
		.file-preview div.flex.config-area label.frappe-checkbox {
			display: none !important;
		}

		.comment-wrapper,
		.comment-box {
			display: none !important;
		}



		/* ---------------- DESK SIDEBAR SELECTED ---------------- */
		.desk-sidebar-item.standard-sidebar-item.selected {
			background: linear-gradient(
				90deg, 
				var(--ws-accent-light), 
				var(--ws-accent)
			) !important;
			font-weight: 700 !important;
		}



		/* ---------------- COMPACT FORM TABS ---------------- */
		.form-tabs-list {
			border-radius: var(--ws-radius-standard);
			box-shadow: 0 2px 8px rgba(0,0,0,0.03);
			padding: 2px 4px;
			margin-bottom: 20px;
			display: flex;
			justify-content: center;
		}

		.form-tabs-list .nav.form-tabs {
			display: flex;
			border-bottom: none;
			width: 100%;
		}

		.form-tabs-list .nav-link {
			border-radius: 4px;
			padding: 8px 18px;
			font-weight: 600;
			font-size: 14px;
			border: none;
			transition: 0.16s;
		}

		.form-tabs-list .nav-link.active {
			padding: auto;
			box-shadow: 0 2px 8px rgba(0,0,0,0.08);
			font-weight: 700;
		}
	"""
